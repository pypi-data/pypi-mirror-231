class PatchingError(Exception):
    pass


class patch_aiohttp_requests(object):
    methods = ['get', 'post', 'put', 'patch', 'delete', 'request']

    def __init__(self, patches=None):
        self.patches = [self._prepare_patch(patch) for patch in patches] if patches else []
        self._remaining = list(self.patches)

    def _prepare_patch(self, patch):
        return patch if isinstance(patch, AioHttpPatch) else AioHttpPatch(*patch)

    def __enter__(self):
        def mock_side_effect(actual_http_method, *args, **kwargs):
            for i, patch in enumerate(self._remaining):
                if patch.match(actual_http_method, *args, **kwargs):
                    patch.call_args = args, kwargs
                    del self._remaining[i]
                    self._remaining.extend(self._prepare_patch(p) for p in patch.subsequent)
                    return patch.get_response()
            else:
                raise PatchingError(f'No matching response: attempting "{actual_http_method}" to "{args[0]}"')

        def start_patchers(method):
            requests_patcher = patch(f'aiohttp.ClientSession.{method}')
            mocked_method_call = requests_patcher.start()

            setattr(self, f'{method}_requests_patcher', requests_patcher)
            setattr(self, f'mocked_{method}', mocked_method_call)

            mocked_method_call.side_effect = partial(mock_side_effect, method)

        for method in self.methods:
            start_patchers(method)
        return self

    def __exit__(self, exc_type, *exc):
        if exc_type == PatchingError:
            return

        assert not self._remaining

        self.mocks = {method: getattr(self, f'mocked_{method}')
                      for method in self.methods}


class AioHttpPatch(object):
    def __init__(self, method, url, response_status, response_content, response_headers=None, subsequent=None):
        self.method = method
        self.url = url
        self.response_status = response_status
        self.response_content = response_content
        self.response_headers = response_headers
        self.subsequent = subsequent or []

    def get_response(self):
        response = AsyncMock()
        response.status = self.response_status
        if self.response_headers:
            response.headers = self.response_headers

        if isinstance(self.response_content, str):
            response.text.return_value = self.response_content
        elif isinstance(self.response_content, (dict, list)):
            response.json.return_value = self.response_content
        else:
            raise NotImplementedError(
                f'Cannot build mocked response for type {resp.__class__}')

        mock = AsyncMock()
        mock.__aenter__.return_value = response
        return mock

    def match(self, actual_http_method, *args, **kwargs):
        return self.method == actual_http_method and self.url in args[0]
