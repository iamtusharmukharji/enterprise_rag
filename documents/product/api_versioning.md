---
document_id: PROD-API-001
department: Product
category: api_versioning
version: 2
effective_date: 2026-07-10
access_level: internal
title: API Versioning and Deprecation Policy
---

# API Versioning Policy

## Versioning Strategy
Public APIs use explicit major versions in the URL, such as `/v1/orders` and `/v2/orders`.

Backward-compatible additions may be introduced within an existing major version. Breaking changes require a new major version.

## Deprecation
An API version should receive at least 6 months of deprecation notice before shutdown unless a security emergency requires faster retirement.

Deprecation notices must identify the replacement version, migration guidance, and planned shutdown date.

## Compatibility
Removing fields, changing field meaning, changing required parameters, or changing response semantics in a way that breaks existing clients is considered a breaking change.

Adding an optional response field is normally backward-compatible.

## Security Exceptions
A vulnerable endpoint may be disabled sooner than the normal deprecation period when continuing operation presents material security risk. The security team and API owner must document the decision.

## Migration
Migration documentation should include endpoint mappings, changed schemas, authentication differences, examples, and known incompatibilities.

## Related Policies
Release Process governs product readiness. Security Guidelines govern security controls for APIs.
