# Automated SSL Certificate Expiry Monitoring with Slack Notifications
<br>
This project implements a comprehensive system for monitoring SSL certificate expiration dates. It leverages the following technologies:

Cron Job: Scheduled tasks run at regular intervals to automate SSL expiry checks. <br>
GitHub Actions: Manages the workflow, including triggering cron jobs and deploying code updates. <br>
SSL Expiry Check Script: Checks the SSL certificate validity of a website and extracts the expiry date. <br>
Slack Integration: Sends notifications to a designated Slack channel, informing users about remaining days until SSL expiry. <br>
This system provides several benefits:

Proactive Management: Avoids certificate expiration and potential website downtime by providing timely alerts. <br>
Automated Workflow: Eliminates manual checks and simplifies SSL certificate management. <br>
Centralized Monitoring: Keeps track of SSL expirations for multiple websites (if desired). <br>
Clear Communication: Delivers expiry information directly to relevant individuals through Slack notifications. <br>
