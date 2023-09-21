# AutoLinkedIn

Elevate your LinkedIn game with **AutoLinkedIn**, a Python package designed for automating routine LinkedIn tasks. Whether you want to connect with specific users, manage connection requests, or optimize your LinkedIn networking, this package has you covered.

### Key Features

- **Login to LinkedIn**: Seamlessly access your LinkedIn account.
- **Send Connection Requests**: Customize your connection requests by filtering users based on mutual connections, user types, and more.
- **Accept Connection Requests**: Simplify the process of accepting incoming connection requests.
- **Delete/Withdraw Sent Requests**: Keep your connection list clean by removing outdated sent requests.
- **Smart Follow-Unfollow**: Automatically manage connections, delete aged requests, and maximize your daily interactions within LinkedIn's limits.
- **Background Mode**: Run all tasks in the background mode without interfering with your regular work.

**Note**: **AutoLinkedIn** has been tested on macOS and is expected to work on Linux/Unix environments as well. If you encounter any issues while running the scripts, feel free to raise an issue or submit a pull request.

### Getting Started

To get started with **AutoLinkedIn**, first, install the package from PyPi using the following command:

```bash
pip install autolinkedin
```

Next, you can run and test the package by creating a script similar to `samplelinkedin/scripts/sample_script.py`. Start by running your script with `LINKEDIN_BROWSER_HEADLESS=0` to ensure everything works as expected. Once you're confident, switch to `LINKEDIN_BROWSER_HEADLESS=1` to run your script in the background.

Here's a simplified example of running **AutoLinkedIn**:

```python
from autolinkedin.linkedin import LinkedIn

settings = {
    "LINKEDIN_USER": "<your_username>",
    "LINKEDIN_PASSWORD": "<your_password>",
    "LINKEDIN_BROWSER": "Chrome",
    "LINKEDIN_BROWSER_HEADLESS": 0,
    "LINKEDIN_PREFERRED_USER": "/path/to/preferred/user/text_doc.text",
    "LINKEDIN_NOT_PREFERRED_USER": "/path/to/not/preferred/user/text_doc.text",
}

with LinkedIn(
        username=settings.get("LINKEDIN_USER"),
        password=settings.get("LINKEDIN_PASSWORD"),
        browser=settings.get("LINKEDIN_BROWSER"),
        headless=bool(settings.get("LINKEDIN_BROWSER_HEADLESS")),
) as ln:
    # Perform LinkedIn actions here
    ln.login()
    ln.remove_sent_invitations(older_than_days=14)
    last_week_invitations = ln.count_invitations_sent_last_week()

    ln.send_invitations(
        max_invitations=max(ln.WEEKLY_MAX_INVITATION - last_week_invitations, 0),
        min_mutual=10,
        max_mutual=450,
        preferred_users=["Quant"],  # file_path or list of features
        not_preferred_users=["Sportsman"],  # file_path or list of features
        view_profile=True,  # (recommended) view profile of users you sent connection requests to
    )

    ln.accept_invitations()

    # Customize your actions as needed
    # ...

    # Alternatively, use the smart follow-unfollow method for a streamlined approach
    ln.smart_follow_unfollow(
        min_mutual=0,
        max_mutual=500,
        withdraw_invite_older_than_days=14,
        max_invitations_to_send=0,
        users_preferred=settings.get("LINKEDIN_PREFERRED_USER") or [],
        users_not_preferred=settings.get("LINKEDIN_NOT_PREFERRED_USER") or [],
    )
```

### Command Line Usage

**AutoLinkedIn** provides a convenient command-line interface for easy interaction. You can execute tasks directly from the command line with options like:

```bash
python -m autolinkedin -h
```

This command will display a list of available options, allowing you to configure and execute LinkedIn tasks without writing scripts.

### Setting Up Cron Jobs

To schedule recurring tasks, you can set up cron jobs using **AutoLinkedIn**. Here's how:

1. Start with the following commands. (Use `example.env` as a reference while setting `.env` values)

```bash
python -m autolinkedin --env .env
```

2. You can supply `--rmcron` to remove existing cron jobs:

```bash
python -m autolinkedin --rmcron --cronuser osuser
```

3. To create a new cron job, specify the desired settings:

```bash
python -m autolinkedin --cronfile .cron.env --cronuser osuser --cronhour 23
```

These cron jobs enable you to automate your LinkedIn tasks at specific times, enhancing your networking efficiency.

### Extras

**LinkedInPy** heavily relies on another package named [SeleniumTabs](https://github.com/inquilabee/selenium-tabs). Feel free to explore that package for additional functionality.

### TODOs

- Enhance documentation
- Include comprehensive tests
