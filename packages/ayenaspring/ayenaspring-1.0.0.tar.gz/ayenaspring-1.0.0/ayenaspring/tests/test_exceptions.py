import pickle

import pytest

import ayenaspring

EXCEPTION_TEST_CASES = [
    ayenaspring.InvalidRequestError(
        "message",
        "param",
        code=400,
        http_body={"test": "test1"},
        http_status="fail",
        json_body={"text": "iono some text"},
        headers={"request-id": "asasd"},
    ),
    ayenaspring.error.AuthenticationError(),
    ayenaspring.error.PermissionError(),
    ayenaspring.error.RateLimitError(),
    ayenaspring.error.ServiceUnavailableError(),
    ayenaspring.error.SignatureVerificationError("message", "sig_header?"),
    ayenaspring.error.APIConnectionError("message!", should_retry=True),
    ayenaspring.error.TryAgain(),
    ayenaspring.error.Timeout(),
    ayenaspring.error.APIError(
        message="message",
        code=400,
        http_body={"test": "test1"},
        http_status="fail",
        json_body={"text": "iono some text"},
        headers={"request-id": "asasd"},
    ),
    ayenaspring.error.OpenAIError(),
]


class TestExceptions:
    @pytest.mark.parametrize("error", EXCEPTION_TEST_CASES)
    def test_exceptions_are_pickleable(self, error) -> None:
        assert error.__repr__() == pickle.loads(pickle.dumps(error)).__repr__()
