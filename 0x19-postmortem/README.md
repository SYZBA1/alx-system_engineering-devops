
# Postmortem: Web Service Outage

# image 


file:///C:/Users/SAMI/Downloads/DALL%C2%B7E%202024-09-24%2014.50.57%20-%20A%20detailed%20visual%20of%20a%20web%20service%20outage%20postmortem.%20The%20scene%20shows%20a%20timeline%20starting%20with%20an%20alert%20and%20ending%20with%20the%20restoration%20of%20services.%20I.webp

# Issue Summary


- Duration: 3 hours, from 9:00 AM to 12:00 PM (UTC).  
- Impact: 70% of users were unable to access the service due to a high load time and intermittent downtime. API calls failed for external services, resulting in poor user experience.  
- Root Cause: A misconfigured load balancer in production led to increased server load, causing performance degradation and service downtime.

# Timeline
- 9:00 AM: Alert from monitoring system due to high response times.
- 9:05 AM: Engineering team notified.
- 9:10 AM: Initial investigation identified high CPU usage on web servers.
- 9:30 AM: Engineers suspected database locking issues, but further investigation revealed no locking problems.
- 10:00 AM: Misleading path investigated the server's auto-scaling group, assuming scaling failure.
- 11:00 AM: Issue escalated to DevOps team for load balancer configuration review.
- 11:30 AM: Misconfiguration detected in load balancer rules, restricting traffic distribution.
- 12:00 PM: Load balancer reconfigured, and service restored.

# Root Cause and Resolution
- Root Cause: A recent update to the load balancer incorrectly limited traffic routing to fewer servers than needed. This overload led to increased CPU usage and eventual failure to handle incoming requests.
- Resolution: The load balancer configuration was corrected, rebalancing traffic across all servers. A rolling restart of affected servers was performed to stabilize services.

# Corrective and Preventative Measures
- Improve load balancer configuration validation during updates.
- Implement more granular monitoring for traffic distribution and server load balancing.
- Tasks:
  - Add automated validation checks for load balancer updates.
  - Implement an alert system for abnormal traffic distribution.
  - Conduct a post-update review process for infrastructure changes.

# The Tale of the Burnout Server
Issue Summary
- Duration: 4 hours (2:00 PM - 6:00 PM UTC)  
- Impact: 85% of users encountered the dreaded "spinning wheel of doom" as our servers waved a white flag and crashed.  
- Root Cause: An overenthusiastic bot decided to hammer our servers with requests, overloading the system. Guess they loved us a bit too much.

# Timeline
- 2:00 PM: Monitoring system beeps: "High response times detected!"  
- 2:05 PM: Engineer: “Maybe it’s just traffic?” Proceeds to refresh page...nothing.  
- 2:20 PM: Suspected API bottleneck; investigation begins.  
- 3:00 PM: Investigation veers towards database slowness. False lead.  
- 4:00 PM: Security review identifies a bot flood from the abyss.  
- 5:00 PM: Traffic rerouted, bot-blocking firewall enabled.  
- 6:00 PM: Back to normal, servers breathing again.

# Root Cause and Resolution
- Root Cause: An automated bot slammed our servers with excessive requests, overwhelming system capacity.  
- Resolution: Updated the firewall to block suspicious traffic and adjusted rate-limiting for incoming requests.

# Preventative Measures
- Add anti-bot measures (CAPTCHA, rate-limiting).  
- Enhance traffic monitoring to detect abnormal patterns early.  
- Tasks:  
  - Implement advanced bot detection.  
  - Upgrade firewall settings.  
  - Test disaster recovery plans (again).

# Diagram
https://www.reddit.com/r/Games/comments/bed5fb/servers_for_the_2008_version_of_burnout_paradise/

