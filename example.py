import asyncio
import asyncio, wrapper

async def main() -> None:

    credentials = wrapper.Credentials(
        username="1234567",
        password="abcdefg"
    )

    example = wrapper.API(credentials)

    await example.notes(limit=10)       # Get the last ten notes.
    await example.timetable(day="wed")  # Get the timetable for Wednesday.
    await example.study_deficit()       # Get any study deficit.

asyncio.get_event_loop().run_until_complete(main())