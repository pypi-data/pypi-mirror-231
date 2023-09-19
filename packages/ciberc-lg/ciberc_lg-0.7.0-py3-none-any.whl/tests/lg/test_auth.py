from lg import auth


def test_lg_auth(lg_auth: auth.LGAuth):
    t = lg_auth.get_access_token()
    assert isinstance(t, str)


# class TestLGAuth:
#     def test_check_token_expiration(lg_auth):
#         lg_auth
