import pickle

import pytest

import ayena

EXCEPTION_TEST_CASES = [
    ayena.InvalidRequestError(
        "message",
        "param",
        code=400,
        http_body={"test": "test1"},
        http_status="fail",
        json_body={"text": "iono some text"},
        headers={"request-id": "asasd"},
    ),
    ayena.error.AuthenticationError(),
    ayena.error.PermissionError(),
    ayena.error.RateLimitError(),
    ayena.error.ServiceUnavailableError(),
    ayena.error.SignatureVerificationError("message", "sig_header?"),
    ayena.error.APIConnectionError("message!", should_retry=True),
    ayena.error.TryAgain(),
    ayena.error.Timeout(),
    ayena.error.APIError(
        message="message",
        code=400,
        http_body={"test": "test1"},
        http_status="fail",
        json_body={"text": "iono some text"},
        headers={"request-id": "asasd"},
    ),
    ayena.error.OpenAIError(),
]


class TestExceptions:
    @pytest.mark.parametrize("error", EXCEPTION_TEST_CASES)
    def test_exceptions_are_pickleable(self, error) -> None:
        assert error.__repr__() == pickle.loads(pickle.dumps(error)).__repr__()
