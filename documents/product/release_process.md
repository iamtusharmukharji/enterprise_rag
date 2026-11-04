---
document_id: PROD-REL-001
department: Product
category: release_management
version: 3
effective_date: 2026-06-20
access_level: internal
title: Product Release Process
---

# Product Release Process

## Release Stages
A product release moves through planning, development, QA validation, release candidate approval, production deployment, and post-release monitoring.

## Release Candidate
A release candidate may be promoted to production only after QA has completed the agreed test scope and the product owner has approved release readiness.

Critical defects must be resolved or explicitly accepted by the product owner and engineering owner before release.

## Change Risk
High-risk releases should include a documented rollout plan, monitoring criteria, and rollback plan.

Feature flags should be used when practical for changes that benefit from controlled exposure.

## Production Deployment
The Deployment Policy governs the technical production deployment. The Release Process determines product readiness and business approval.

## Post-Release Monitoring
The release owner should monitor error rates, customer-impacting metrics, and key product workflows after deployment.

For high-risk releases, enhanced monitoring should continue for at least 60 minutes after full rollout.

## Release Notes
Customer-visible changes should have release notes. Internal-only changes should still document operationally relevant behavior changes.

## Related Policies
Deployment Policy governs deployment mechanics. Incident Management governs response when a release causes a production incident.
