---
document_id: ENG-SEC-001
department: Engineering
category: security
version: 4
effective_date: 2026-07-01
access_level: internal
title: Engineering Security Guidelines
---

# Engineering Security Guidelines

## Secrets
API keys, passwords, private keys, database credentials, and access tokens must never be committed to source control.

Production secrets must be stored in the approved secrets-management system. Environment variables may be used for runtime injection but must not be used as a reason to commit secrets into configuration files.

## Authentication
Production services must use approved authentication mechanisms. Passwords must never be stored in plaintext. Authentication failures should be logged without recording passwords, tokens, or other secret values.

## Authorization
Authorization must be enforced server-side. Client-side checks are not sufficient for protecting restricted operations.

Services should follow least privilege and grant only the permissions required for a task.

## Data Protection
Sensitive data must be encrypted in transit. Production databases containing confidential or restricted data must use encryption at rest.

Logs must avoid sensitive personal data, authentication credentials, and full payment-card information.

## Dependencies
Third-party dependencies should be pinned or otherwise controlled through approved dependency-management practices. Critical security updates should be prioritized according to the vulnerability's severity and exposure.

## Remote Access
Remote employees must use company-managed devices and the approved VPN when accessing protected internal systems from untrusted networks. Public or shared computers must not be used for privileged company access.

## Security Incidents
Suspected credential compromise must be reported immediately to the security team and handled as a security incident. Engineers must not delete or alter relevant logs before security investigation is complete.

## Related Policies
Code review requirements for security-sensitive changes are defined in Code Review Guidelines. Incident response timelines are defined in Incident Management.
