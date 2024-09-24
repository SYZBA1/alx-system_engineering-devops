
# Postmortem: Web Service Outage

# image 


file:///C:/Users/SAMI/Downloads/DALL%C2%B7E%202024-09-24%2014.50.57%20-%20A%20detailed%20visual%20of%20a%20web%20service%20outage%20postmortem.%20The%20scene%20shows%20a%20timeline%20starting%20with%20an%20alert%20and%20ending%20with%20the%20restoration%20of%20services.%20I.webp

#Issue Summary


- Duration: 3 hours, from 9:00 AM to 12:00 PM (UTC).  
- Impact: 70% of users were unable to access the service due to a high load time and intermittent downtime. API calls failed for external services, resulting in poor user experience.  
- Root Cause: A misconfigured load balancer in production led to increased server load, causing performance degradation and service downtime.

#Timeline
- 9:00 AM: Alert from monitoring system due to high response times.
- 9:05 AM: Engineering team notified.
- 9:10 AM: Initial investigation identified high CPU usage on web servers.
- 9:30 AM: Engineers suspected database locking issues, but further investigation revealed no locking problems.
- 10:00 AM: Misleading path investigated the server's auto-scaling group, assuming scaling failure.
- 11:00 AM: Issue escalated to DevOps team for load balancer configuration review.
- 11:30 AM: Misconfiguration detected in load balancer rules, restricting traffic distribution.
- 12:00 PM: Load balancer reconfigured, and service restored.

#Root Cause and Resolution
- Root Cause: A recent update to the load balancer incorrectly limited traffic routing to fewer servers than needed. This overload led to increased CPU usage and eventual failure to handle incoming requests.
- Resolution: The load balancer configuration was corrected, rebalancing traffic across all servers. A rolling restart of affected servers was performed to stabilize services.

#Corrective and Preventative Measures
- Improve load balancer configuration validation during updates.
- Implement more granular monitoring for traffic distribution and server load balancing.
- Tasks:
  - Add automated validation checks for load balancer updates.
  - Implement an alert system for abnormal traffic distribution.
  - Conduct a post-update review process for infrastructure changes.


