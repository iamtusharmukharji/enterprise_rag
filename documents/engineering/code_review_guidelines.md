---
document_id: ENG-CR-001
department: Engineering
category: code_review
version: 4
effective_date: 2026-05-01
access_level: internal
title: Code Review Guidelines
---

# Code Review Guidelines

## Purpose
Code review protects production quality, security, maintainability, and shared engineering standards.

## Pull Request Requirements
Every production code change must be submitted through a pull request. The pull request should explain the change, testing performed, operational impact, and any migration or rollback considerations.

A pull request should normally be small enough for reviewers to understand the complete change. Large changes should be split when practical.

## Approvals
A normal production change requires at least 1 approving reviewer. Changes affecting authentication, authorization, encryption, payment processing, or security controls require at least 2 approvals, including one reviewer with relevant security ownership.

The author cannot approve their own pull request.

## Testing
Authors are responsible for adding or updating automated tests for changed behavior. Critical-path changes should include unit and integration coverage where applicable.

Reviewers should verify that tests cover failure paths, not only successful execution.

## Review Priorities
Reviewers should prioritize correctness, security, data integrity, concurrency behavior, API compatibility, and operational safety before style preferences.

Blocking comments should identify the risk and, where possible, a concrete improvement.

## Emergency Changes
Emergency production changes may bypass normal review only when delaying the change would create a larger operational or security risk. The change must receive retrospective review within 1 business day.

## Related Policies
Deployment approval and rollback rules are defined in the Deployment Policy. Security-specific implementation expectations are defined in the Security Guidelines.
