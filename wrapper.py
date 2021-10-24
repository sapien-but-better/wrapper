import asyncio, aiohttp, json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Credentials:
    username: str
    password: str

    @property
    def header(self) -> str:
        return json.dumps({"username": self.username, "password": self.password})

@dataclass
class SapienError(Exception):
    message: str
    status_code: str

class API():

    BASE_URL: str = "https://api.sap.morgverd.com/v1/"
    SSL_VERIFICATION: bool = False

    def __init__(self, credentials: Credentials):
        self._credentials = credentials

    @property
    def _headers(self) -> dict:
        return {
            "Accept": "application/json",
            "Authorization": self._credentials.header
        }

    async def _request(self, route: str, arguments: dict = {}, raiseException: bool = False) -> dict:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=self.SSL_VERIFICATION)) as session:
            async with session.get(self.BASE_URL + route, headers=self._headers, params=arguments) as request:
                data = await request.json()

        if not data["success"] and raiseException: raise SapienError(data["error_message"], data["error_status"] if "error_status" in data else 500)
        return data
    
    async def timetable(self, day: Optional[str] = None) -> dict:
        if str(day).lower() not in ["none", "mon", "tue", "wed", "thu", "fri"]: raise ValueError("Invalid timetable day value.")
        return await self._request("timetable", arguments={"day": day})
        
    async def study_deficit(self) -> dict:
        return await self._request("study_deficit")
        
    async def notes(self, limit: Optional[int] = None) -> dict:
        return await self._request("notes", arguments={"limit": limit})
    