---
document_id: ENG-INC-001
department: Engineering
category: incident_management
version: 5
effective_date: 2026-07-15
access_level: internal
title: Incident Management Policy
---

# Incident Management Policy

## Severity Levels
SEV-1 is a critical incident causing widespread customer impact, major data integrity risk, or complete unavailability of a critical service.

SEV-2 is a major incident causing significant customer or business impact but with a viable workaround or limited scope.

SEV-3 is a moderate incident with limited impact and no immediate business-critical consequence.

## Acknowledgement Targets
SEV-1 incidents must be acknowledged within 15 minutes.

SEV-2 incidents must be acknowledged within 30 minutes.

SEV-3 incidents must be acknowledged within 4 business hours.

## Incident Commander
For SEV-1 and SEV-2 incidents, an Incident Commander must be assigned. The Incident Commander coordinates response, assigns owners, maintains the incident timeline, and decides when the incident can be downgraded or closed.

## Escalation
A SEV-1 incident must page the on-call engineer immediately and notify the service owner. If customer impact continues for more than 30 minutes, the engineering director should be notified.

Security incidents involving suspected credential compromise must also follow the Security Guidelines and be escalated to the security team.

## Communication
The incident channel should contain the current impact, actions in progress, owners, and next update time.

Customer-facing communication must be coordinated by the incident commander with Support or Communications.

## Post-Incident Review
SEV-1 incidents require a post-incident review within 5 business days. The review should identify root causes, contributing factors, detection gaps, and corrective actions.

## Related Policies
Deployment rollback is covered by Deployment Policy. Security incidents additionally follow Security Guidelines.
