# MCP Service Offers

> Pricing below is provisional and intended for sales discovery. Adjust based on client calls, delivery experience, and willingness to pay.

## 1. MCP Development

**Starting price:** $20,000 one-time

Design, build, test, and launch a production-ready MCP server that makes the client's existing application available to AI agents.

### Included

#### Core workflows
- Up to **5 core user workflows**
- Workflows are scoped around user outcomes, not API endpoints or raw tool count
- Examples:
  - Find a movie and buy tickets
  - Reorder a previous food order
  - Search a product catalog and check availability
  - Create an event and invite attendees
- Additional workflows can be added later as separate scope

#### Tool and interface design
- MCP tools designed around agent usability rather than mechanically exposing the existing API
- Clear tool descriptions, inputs, outputs, and error behavior
- Appropriate safeguards around state-changing or destructive actions

#### Authentication and permissions
- Integration with the client's existing authentication model
- User- and tenant-level authorization where required
- Safe handling of credentials, tokens, and secrets

#### Agent compatibility
- Validation against major MCP-compatible clients relevant to the launch
- Testing of representative agent behaviors and tool-use patterns

#### Evaluation and hardening
- Functional testing of the supported workflows
- Error handling and retries where appropriate
- Validation of authorization boundaries and write actions
- Regression coverage for critical workflows
- Basic performance and reliability testing

#### Deployment and launch
- Production deployment of the MCP server
- Configuration of the production environment
- Assistance with MCP registry/listing or client connection setup where applicable
- Launch verification

#### Documentation and handoff
- Technical documentation
- Tool/workflow reference
- Deployment and operational notes
- Engineering handoff session

### Development downsell levers

The implementation can be reduced in price by reducing **scope**, not by removing baseline security or correctness.

Typical adjustments may include:

- Fewer workflows, e.g. 2–3 instead of 5
- Support for one primary MCP client instead of broader compatibility testing
- Client-managed deployment instead of fully managed launch
- Reduced documentation and handoff
- Simpler authentication where the existing application already supports it cleanly
- Reduced evaluation depth for lower-risk/read-only use cases

A focused launch might target approximately **$16,000** by limiting the initial workflow scope while preserving production quality.

### Non-negotiable baseline

Every implementation should still include:
- Secure handling of authentication and credentials
- Correct authorization behavior
- Sensible error handling
- Safe handling of state-changing actions
- Sufficient testing to support a production launch

---

## 2. Managed MCP Operations

**Starting price:** $1,000/month

Ongoing operation and maintenance of the MCP server after launch so the client does not need to dedicate internal engineering time to keeping the service healthy and compatible.

### Included

#### Production infrastructure
- Managed production deployment
- Infrastructure configuration and routine changes
- Backups where applicable
- Basic redundancy and recovery planning

#### Monitoring and incident detection
- 24/7 automated service monitoring
- Health checks and alerting
- Detection of availability and integration failures
- Investigation of service issues within the agreed support window

#### MCP and dependency maintenance
- MCP protocol and client compatibility updates
- Dependency updates
- Routine maintenance and regression testing
- Updates required by supported upstream APIs

#### Security and access management
- Security patching
- Secrets and credential configuration
- Authentication configuration maintenance
- Logging and audit support where applicable

#### Support and service level
- Defined support channel
- Agreed response-time target during supported hours
- Best-effort response outside the support window unless a higher SLA is purchased
- Operational guidance when incidents involve the client's upstream systems

### Managed operations downsell levers

Monthly pricing can be adjusted by reducing the operational responsibility accepted by R5 AI.

Possible adjustments include:

- Automated monitoring only; client owns incident response
- Business-hours support instead of extended or priority coverage
- Client-managed infrastructure
- Updates billed separately instead of included
- Client-managed security and credential changes
- No recurring operational review or reporting

### Higher-service options

Higher monthly tiers can add:

- 24/7 human incident response
- Faster guaranteed response times
- Stronger uptime commitments
- Dedicated or isolated infrastructure
- Higher redundancy requirements
- Advanced observability and reporting
- Load and capacity planning
- Formal incident management and postmortems
- Compliance-specific operational requirements

---

## Pricing principle

Pricing reflects the **scope and responsibility R5 AI accepts**, not just compute or request volume.

For development, the primary pricing lever is the number and complexity of supported user workflows.

For managed operations, the primary pricing lever is how much operational responsibility the client transfers to R5 AI: infrastructure ownership, monitoring, incident response, maintenance, security, and SLA commitments.

The objective is to make pricing transparent enough that scope can be adjusted during a sales conversation without arbitrary discounting.
