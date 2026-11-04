---
document_id: ENG-DEPLOY-001
department: Engineering
category: deployment
version: 3
effective_date: 2026-06-01
access_level: internal
title: Deployment and Release Deployment Policy
---

# Deployment Policy

## Environments
Northstar Systems uses development, staging, and production environments. Production deployments must be traceable to a version-controlled artifact.

## Standard Deployment
A standard production deployment requires:
1. successful automated CI checks;
2. required pull-request approvals;
3. successful staging validation;
4. deployment authorization from the service owner or designated release approver.

## Deployment Windows
Standard production deployments should occur during approved deployment windows. High-risk changes should use a change ticket and an explicit rollback plan.

Emergency deployments may occur outside the standard window when required to restore service or mitigate a critical security issue.

## Rollback
Every production deployment must have a rollback strategy. If automated rollback is available, it should be validated before release for high-risk changes.

If error rate, latency, or critical functionality exceeds the service's rollback threshold, the release owner should initiate rollback rather than waiting for the normal deployment window.

## Database Changes
Backward-compatible database migrations are required when application and database versions may coexist during a rolling deployment.

Destructive schema changes require a separate migration step after dependent application versions have been retired.

## Observability
Production deployments must expose sufficient logs and metrics to detect deployment-related regressions. Critical services should have dashboards and alerts for error rate and latency.

## Related Policies
Code review requirements are defined in Code Review Guidelines. Incident handling and escalation are defined in Incident Management.
