# ADR-0002: Zotero Remains the Bibliographic Source of Truth

- Status: Accepted
- Date: 2026-08-23

## Context

Zotero already manages bibliographic parent records, citation metadata, attachments, and indexed full text.

## Decision

Use Zotero as the bibliographic and PDF-management source of truth. Reference its item and citation keys from derived records instead of creating a second bibliography database.

## Consequences

Library writes remain explicit authorization actions. Workflows must handle Zotero unavailability without inventing metadata.
