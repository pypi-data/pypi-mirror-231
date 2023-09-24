import asyncio
from dataclasses import dataclass
from urllib.parse import urljoin
import httpx
from httpx import HTTPStatusError


@dataclass
class UserInfo:
    username: str
    avatar_url: str
    name: str
    public_repos_count: int


class GithubClient:
    def __init__(self, base_url: str, token: str) -> None:
        self._url = base_url.removesuffix('/')
        self._token = token

    async def _make_request(self, endpoint: str) -> dict:
        headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'Authorization': f'Bearer {self._token}'
        }
        async with httpx.AsyncClient() as session:
            response = await session.get(urljoin(self._url, endpoint), headers=headers)
            response.raise_for_status()
            return response.json()

    async def get_user_info(self, username: str) -> UserInfo:
        result = await self._make_request(f'users/{username}')
        return UserInfo(
            username=result['login'],
            avatar_url=result['avatar_url'],
            name=result['name'],
            public_repos_count=result['public_repos'],
        )


async def main(default_profile: str = 'nmzgnv') -> None:
    token = input(
        'Paste your github access token '
        '(https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)\n'
        '> '
    ).strip()
    user_profile = input(f'Input github username (or blank to get "{default_profile}")\n> ').strip() or default_profile
    client = GithubClient('https://api.github.com/', token)
    try:
        user_info = await client.get_user_info(user_profile)
    except HTTPStatusError as e:
        print(f'Something went wrong: {e.response.text}')
        return

    print(
        f'Github profile: {user_info.username}\n'
        f'Name: {user_info.name}\n'
        f'Avatar: {user_info.avatar_url}\n'
        f'Public repositories count: {user_info.public_repos_count}'
    )


if __name__ == '__main__':
    asyncio.run(main())
