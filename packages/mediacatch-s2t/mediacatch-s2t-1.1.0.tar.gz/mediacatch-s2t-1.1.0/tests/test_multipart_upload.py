from unittest import mock

import pytest
import responses

from mediacatch_s2t import (
    URL, MULTIPART_UPLOAD_CREATE_ENDPOINT, MULTIPART_UPLOAD_URL_ENDPOINT,
    MULTIPART_UPLOAD_COMPLETE_ENDPOINT,
    UPDATE_STATUS_ENDPOINT
)
from mediacatch_s2t.uploader import (
    ChunkedFileUploader, Uploader, UploaderException)


class TestMultipartUpload:
    create_multipart_url = f"{URL}{MULTIPART_UPLOAD_CREATE_ENDPOINT}"
    get_signed_url = f"{URL}{MULTIPART_UPLOAD_URL_ENDPOINT}"
    complete_upload_url = f"{URL}{MULTIPART_UPLOAD_COMPLETE_ENDPOINT}"
    update_status_url = f"{URL}{UPDATE_STATUS_ENDPOINT}"
    chunk_maxsize = 20480000
    filesize = (500 * chunk_maxsize) + 10000
    file_id = "644f6676997bc2477563246e"
    upload_id = "2~iRldDSPjP1cJCXg-7NmR9Sd4xpX_Cii"
    mime_file = {
        "duration": 1000,
        "filename": "file-test",
        "file_ext": ".mp4",
        "filesize": filesize,
        "language": "da",
    }

    @pytest.fixture(autouse=True)
    def _mock_pathlib_path(self):
        with mock.patch("pathlib.Path") as mock_Path:
            def side_effect():
                return True
            mock_Path.return_value.name = 'file-test'
            mock_Path.return_value.suffix = '.mp4'
            mock_Path.return_value.is_file.side_effect = side_effect
            yield mock_Path

    @pytest.fixture(autouse=True)
    def _mock_os_getsize(self):
        with mock.patch("os.path.getsize") as mock_getsize:
            mock_getsize.return_value = self.filesize
            yield mock_getsize

    @pytest.fixture(autouse=True)
    def _mock_builtins_open(self):
        with mock.patch("builtins.open", mock.mock_open(read_data="data")) as mock_open:
            yield mock_open

    @pytest.fixture(autouse=True)
    def _mock_get_duration(self):
        with mock.patch("mediacatch_s2t.uploader.ChunkedFileUploader.get_duration") as mock_duration:
            mock_duration.return_value = 100000, {}
            yield mock_duration

    @pytest.fixture(autouse=True)
    def _mock_chop_and_upload_chunk(self):
        with mock.patch("mediacatch_s2t.uploader.ChunkedFileUploader.chop_and_upload_chunk") as mocker:
            mocker.return_value = None
            yield mocker


    @pytest.fixture()
    def _mock_endpoints(self):
        with responses.RequestsMock() as resp:
            resp.add(
                responses.POST,
                self.create_multipart_url,
                status=200,
                json={
                    "file_id": self.file_id,
                    "chunk_maxsize": self.chunk_maxsize,
                    "total_chunks": 500 + 1,
                    "upload_id": self.upload_id
                }
            )
            resp.add(
                responses.POST,
                url=self.complete_upload_url,
                status=201
            )
            resp.add(
                responses.POST,
                url=self.update_status_url,
                status=201
            )
            yield resp

    @responses.activate
    def test_create_multipart_upload_return_success(self):
        responses.add(
            responses.POST,
            self.create_multipart_url,
            status=200,
            json={
                "file_id": self.file_id,
                "chunk_maxsize": self.chunk_maxsize,
                "total_chunks": 500 + 1,
                "upload_id": self.upload_id
            }
        )
        file = ChunkedFileUploader(
            file='file-test.mp4',
            api_key='test-key'
        )
        result = file.create_multipart_upload(self.mime_file)
        assert result == {
            "file_id": self.file_id,
            "chunk_maxsize": self.chunk_maxsize,
            "total_chunks": 500 + 1,
            "upload_id": self.upload_id
        }

    @responses.activate
    def test_get_signed_url_return_url(self):
        responses.add(
            responses.POST,
            url=self.get_signed_url,
            status=200,
            json={
                "file_id": self.file_id,
                "upload_id": self.upload_id,
                "part_number": 1,
                "url": "signed-upload-url"
            }
        )
        file = ChunkedFileUploader(
            file='file-test.mp4',
            api_key='test-key'
        )
        result = file._get_signed_url(1)
        assert result == "signed-upload-url"

    @responses.activate
    @mock.patch("mediacatch_s2t.uploader.ChunkedFileUploader._get_signed_url")
    def test_upload_part_return_etag(self, mocker):
        mocker.return_value = "http://signed-upload-url"

        responses.add(
            responses.PUT,
            "http://signed-upload-url",
            status=200,
            headers={
                'ETag': 'etag-from-s3'
            }
        )

        file = ChunkedFileUploader("file-test.mp4", "test-key")
        url = file._get_signed_url(1)
        assert url == "http://signed-upload-url"
        file_data = b''
        etag = file._upload_data_chunk_to_bucket(url, file_data)
        assert etag == 'etag-from-s3'

    def test_upload_file(self, _mock_endpoints):
        chunked_file = ChunkedFileUploader("file-test.mp4", "test-key")

        assert chunked_file._is_file_exist() is True

        file_duration, msg = chunked_file.get_duration()
        assert file_duration == 100000

        assert chunked_file.filename == "file-test"
        assert chunked_file.file_ext == ".mp4"
        assert chunked_file.filesize == 10240010000
        assert chunked_file.language == 'da'

        mime_file = {
            "duration": file_duration,
            "filename": chunked_file.filename,
            "file_ext": chunked_file.file_ext,
            "filesize": chunked_file.filesize,
            "language": chunked_file.language,
        }
        meta = chunked_file.create_multipart_upload(mime_file)
        chunked_file._set_metadata(
            file_id=meta["file_id"],
            chunk_maxsize=meta["chunk_maxsize"],
            total_chunks=meta["total_chunks"],
            upload_id=meta["upload_id"]
        )
        assert chunked_file.file_id == self.file_id
        assert chunked_file.chunk_maxsize == self.chunk_maxsize
        assert chunked_file.total_chunks == 501
        assert chunked_file.upload_id == self.upload_id

        chunked_file.chop_and_upload_chunk()

        assert chunked_file.complete_the_upload() is True

        link = 'https://s2t.mediacatch.io/result?id=644f6676997bc2477563246e&api_key=test-key'
        assert chunked_file._get_transcript_link() == link

        result = chunked_file.upload_file()
        assert result == {
            "url": link,
            "status": "uploaded",
            "estimated_processing_time": 10,
            "message": "The file has been uploaded."
        }


class TestUploaderMethod:
    @pytest.fixture()
    def _mock_is_file_exist_true(self):
        with mock.patch(
                "mediacatch_s2t.uploader.Uploader._is_file_exist") as mocker:
            mocker.return_value = True
            yield mocker

    @mock.patch("os.path.getsize", return_value=10240010000)
    def test_is_multipart_upload_return_true(self, mocker, _mock_is_file_exist_true):
        file = Uploader("file-test.mp4", "test-key")
        assert file.is_multipart_upload() is True

    @mock.patch("os.path.getsize", return_value=10)
    def test_is_multipart_upload_return_false(self, mocker, _mock_is_file_exist_true):
        file = Uploader("file-test.mp4", "test-key")
        assert file.is_multipart_upload() is False

    def test_is_multipart_upload_file_not_exists(self):
        file = Uploader("file-test.mp4", "test-key")
        assert file.is_multipart_upload() is False


    def test_is_response_error_return_true(self):
        response = mock.Mock()
        response.status_code = 401
        response.json.return_value = {"message": "an error 401 test message"}

        file = Uploader("file-test.mp4", "test-key")
        result = file._is_response_error(response)
        assert result == (True, "an error 401 test message")

        response.status_code = 500
        response.json.return_value = {"message": "an error 500 test message"}
        result = file._is_response_error(response)
        assert result == (True, "an error 500 test message")

    @responses.activate
    def test_make_post_request_raise_exception(self):
        responses.add(
            responses.POST,
            url="http://test-500",
            json={"message": "test error 500"},
            status=500
        )

        file = Uploader("file-test.mp4", "test-key")

        with pytest.raises(UploaderException) as exc_info:
            file._make_post_request(url="http://test-500")
        assert str(exc_info.value) == (
            "Error from uploader module: Error during post request "
            "http://test-500; test error 500"
        )
