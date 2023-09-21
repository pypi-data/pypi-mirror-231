import abc
import os
import pathlib
import threading

import requests
import subprocess
import json
from typing import NamedTuple

from langcodes import standardize_tag

from mediacatch_s2t import (
    URL,
    SINGLE_UPLOAD_ENDPOINT, TRANSCRIPT_ENDPOINT, UPDATE_STATUS_ENDPOINT,
    MULTIPART_UPLOAD_CREATE_ENDPOINT, MULTIPART_UPLOAD_URL_ENDPOINT,
    MULTIPART_UPLOAD_COMPLETE_ENDPOINT,
    PROCESSING_TIME_RATIO, MULTIPART_FILESIZE
)
from mediacatch_s2t.helper import update_myself


class FFProbeResult(NamedTuple):
    return_code: int
    json: str
    error: str


class UploaderException(Exception):
    message = "Error from uploader module"

    def __init__(self, cause=None):
        self.cause = cause

    def __str__(self):
        if self.cause:
            return "{}: {}".format(self.message, str(self.cause))
        else:
            return self.message


class UploaderBase(metaclass=abc.ABCMeta):
    def __init__(self, file, api_key, language='da'):
        self.file = file
        self.api_key = api_key
        self.language = standardize_tag(language)
        self.file_id = None

    def _is_file_exist(self):
        return pathlib.Path(self.file).is_file()

    def is_multipart_upload(self) -> bool:
        if self._is_file_exist():
            filesize = os.path.getsize(self.file)
            if filesize > MULTIPART_FILESIZE:
                return True
        return False

    def _is_response_error(self, response):
        if response.status_code >= 400:
            if response.status_code == 401:
                return True, response.json()['message']
            return True, response.json()['message']
        return False, ''

    def _make_post_request(self, *args, **kwargs):
        """Make post request with retry mechanism."""
        call_limit = 3
        is_error, msg = True, "Have not made a request call."
        for _call in range(call_limit):
            response = requests.post(*args, **kwargs)
            is_error, msg = self._is_response_error(response)
            if not is_error:
                break
        if is_error:
            url = kwargs.get('url')
            if not url:
                url, *rest = args
            raise UploaderException(
                f"Error during post request {url}; {msg}"
            )
        return response

    @property
    def _transcript_link(self):
        return f"{URL}{TRANSCRIPT_ENDPOINT}?id={self.file_id}&api_key={self.api_key}"

    @staticmethod
    def _ffprobe(file_path) -> FFProbeResult:
        command_array = ["ffprobe",
                         "-v", "quiet",
                         "-print_format", "json",
                         "-show_format",
                         "-show_streams",
                         file_path]
        result = subprocess.run(command_array, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True)
        return FFProbeResult(return_code=result.returncode,
                             json=json.loads(result.stdout),
                             error=result.stderr)

    def get_duration(self):
        """Get audio track duration of a file.

        :return
        tuple: (duration_in_miliseconds, stream_json | error_msg)
        """
        try:
            probe = self._ffprobe(self.file)
        except OSError as e:
            return 0, 'FFmpeg not installed (sudo apt install ffmpeg)'
        if probe.return_code:
            return 0, probe.error
        else:
            try:
                for stream in probe.json['streams']:
                    if stream['codec_type'] == 'audio':
                        return int(float(stream['duration']) * 1000), stream
                else:
                    return 0, "The file doesn't have an audio track"
            except Exception:
                if 'duration' in probe.json['format']:
                    return int(float(probe.json['format']['duration']) * 1000), probe.json['format']
                else:
                    return 0, "Duration couldn't be found for audio track"

    def estimated_result_time(self, audio_length=0):
        """Estimated processing time in seconds"""

        if not isinstance(audio_length, int):
            return 0
        processing_time = PROCESSING_TIME_RATIO * audio_length
        return round(processing_time / 1000)

    def _post_file(self, url, data):
        with open(self.file, 'rb') as f:
            response = self._make_post_request(
                url,
                data=data,
                files={'file': f}
            )
            return response

    def _get_transcript_link(self):
        self._make_post_request(
            url=f'{URL}{UPDATE_STATUS_ENDPOINT}',
            json={"id": self.file_id},
            headers={
                "Content-type": 'application/json',
                "X-API-KEY": self.api_key,
                "X-LANG": self.language
            }
        )
        return self._transcript_link

    @abc.abstractmethod
    def upload_file(self):
        result = {
            "url": "",
            "status": "uploaded",
            "estimated_processing_time": 0,
            "message": "The file has been uploaded."
        }
        return result


class Uploader(UploaderBase):
    """Uploader Class

    This class is to send a file to the API server.
    The API server currently only allows file less than 4gb
    to be sent with this upload class.
    """

    def _get_upload_url(self, mime_file):
        response = self._make_post_request(
            url=f'{URL}{SINGLE_UPLOAD_ENDPOINT}',
            json=mime_file,
            headers={
                "Content-type": 'application/json',
                "X-API-KEY": self.api_key,
                "X-LANG": self.language
            }
        )
        response_data = json.loads(response.text)
        url = response_data.get('url')
        data = response_data.get('fields')
        _id = response_data.get('id')
        return {
            "url": url,
            "fields": data,
            "id": _id
        }

    def upload_file(self):
        result = {
            "url": "",
            "status": "",
            "estimated_processing_time": 0,
            "message": ""
        }
        if not self._is_file_exist():
            result["status"] = "error"
            result["message"] = "The file doesn't exist"
            return result

        file_duration, msg = self.get_duration()
        if not file_duration:
            result["status"] = "error"
            result["message"] = msg
            return result

        mime_file = {
            "duration": file_duration,
            "filename": pathlib.Path(self.file).name,
            "file_ext": pathlib.Path(self.file).suffix,
            "filesize": os.path.getsize(self.file),
            "language": self.language,
        }
        try:
            _upload_url = self._get_upload_url(mime_file)
            url = _upload_url.get('url')
            data = _upload_url.get('fields')
            self.file_id = _upload_url.get('id')

            self._post_file(url, data)
            transcript_link = self._get_transcript_link()
        except UploaderException as e:
            result["status"] = "error"
            result["message"] = str(e)
            return result

        result = {
            "url": transcript_link,
            "status": "uploaded",
            "estimated_processing_time": self.estimated_result_time(
                file_duration),
            "message": "The file has been uploaded."
        }
        return result


class ChunkedFileUploader(UploaderBase):
    """Multipart Uploader Class

    This class is to split a bigfile into chunked files, and send them
    with multipart upload method.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = pathlib.Path(self.file).name
        self.file_ext = pathlib.Path(self.file).suffix
        self.filesize = os.path.getsize(self.file)

        self.file_id: str = ""
        self.chunk_maxsize: int = 0
        self.total_chunks: int = 0
        self.upload_id: str = ""

        self.endpoint_create: str = f"{URL}{MULTIPART_UPLOAD_CREATE_ENDPOINT}"
        self.endpoint_signed_url: str = f"{URL}{MULTIPART_UPLOAD_URL_ENDPOINT}"
        self.endpoint_complete: str = f"{URL}{MULTIPART_UPLOAD_COMPLETE_ENDPOINT}"
        self.headers: dict = self._get_headers()

        self.etags: list = []

        self.result = {
            "url": "",
            "status": "",
            "estimated_processing_time": 0,
            "message": ""
        }

    def _get_headers(self) -> dict:
        return {
            "Content-type": "application/json",
            "X-API-KEY": self.api_key,
            "X-LANG": self.language
        }

    def _set_result_error_message(self, msg) -> None:
        self.result["status"] = "error"
        self.result["message"] = msg

    def _set_metadata(self, file_id: str, chunk_maxsize: int,
                      total_chunks: int, upload_id: str) -> None:
        self.file_id = file_id
        self.chunk_maxsize = chunk_maxsize
        self.total_chunks = total_chunks
        self.upload_id = upload_id
        return None

    def create_multipart_upload(self, mime_file: dict) -> dict:
        response = self._make_post_request(
            url=self.endpoint_create,
            headers=self.headers,
            json=mime_file
        )
        data: dict = response.json()
        return {
            "chunk_maxsize": data["chunk_maxsize"],
            "file_id": data["file_id"],
            "total_chunks": data["total_chunks"],
            "upload_id": data["upload_id"]
        }

    def chop_and_upload_chunk(self) -> None:
        threads = []
        with open(self.file, 'rb') as f:
            part_number = 0
            while True:
                part_number += 1
                chunk_size = self.chunk_maxsize
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                thread = threading.Thread(target=self.upload_part,
                                          args=(part_number, chunk))
                threads.append(thread)
                thread.start()
        for thread in threads:
            thread.join()
        return None

    def _get_signed_url(self, part_number: int) -> str:
        response = self._make_post_request(
            url=self.endpoint_signed_url,
            headers=self.headers,
            json={
                "file_id": self.file_id,
                "upload_id": self.upload_id,
                "part_number": part_number
            }
        )
        data: dict = response.json()
        return data["url"]

    def _upload_data_chunk_to_bucket(self, url: str, file_data: bytes) -> str:
        response: requests.Response = requests.put(url=url, data=file_data)
        etag: str = response.headers['ETag']
        return etag

    def upload_part(self, part_number: int, file_data: bytes) -> None:
        url = self._get_signed_url(part_number)
        etag = self._upload_data_chunk_to_bucket(url, file_data)
        self.etags.append({'ETag': etag, 'PartNumber': part_number})
        return None

    def complete_the_upload(self) -> bool:
        response: requests.Response = self._make_post_request(
            url=self.endpoint_complete,
            headers=self.headers,
            json={
                "file_id": self.file_id,
                "parts": self.etags
            }
        )
        if response.status_code != 201:
            return False
        return True

    def upload_file(self):
        if not self._is_file_exist():
            self._set_result_error_message("The file doesn't exist")
            return self.result

        file_duration, msg = self.get_duration()
        if not file_duration:
            self._set_result_error_message(msg)
            return self.result

        mime_file = {
            "duration": file_duration,
            "filename": self.filename,
            "file_ext": self.file_ext,
            "filesize": self.filesize,
            "language": self.language,
        }
        try:
            meta = self.create_multipart_upload(mime_file)
            self._set_metadata(
                file_id=meta["file_id"],
                chunk_maxsize=meta["chunk_maxsize"],
                total_chunks=meta["total_chunks"],
                upload_id=meta["upload_id"]
            )

            self.chop_and_upload_chunk()
            self.complete_the_upload()
            transcript_link = self._get_transcript_link()
        except Exception as e:
            self._set_result_error_message(str(e))
            return self.result

        self.result = {
            "url": transcript_link,
            "status": "uploaded",
            "estimated_processing_time": self.estimated_result_time(
                file_duration),
            "message": "The file has been uploaded."
        }
        return self.result


def upload_and_get_transcription(file, api_key, language) -> dict:
    is_multipart_upload: bool = Uploader(
        file, api_key, language).is_multipart_upload()
    if is_multipart_upload:
        result: dict = ChunkedFileUploader(file, api_key, language).upload_file()
    else:
        result: dict = Uploader(file, api_key, language).upload_file()
    update_myself()
    return result
