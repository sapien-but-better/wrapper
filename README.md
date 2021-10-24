# SAP Wrapper

This is a wrapper interface to the [Sapien API](https://github.com/sapien-but-better/api). It is designed to be **very** simplistic wrapper, providing an asynchronous set of functions for easily interacting with the core API. Credentials and Errors are simply provided as dataclasses. The request functions simply return the raw JSON data, and therefore [error checking](https://github.com/sapien-but-better/api#error-checking) is vital.

Please note that this file is designed to just be used internally, and therefore changes may be unpredictable, with breaking changes being introduced without warning. If you intend on using this file in any of your own projects you should write your own wrapper.

## Credential Validation

Please note that due to the design of the API, credentials are **NOT** validated until they actually reach the Sapien system. This means that in the case of incorrect credentials, a JSON response will still be provided.

## Example

```py

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

```
