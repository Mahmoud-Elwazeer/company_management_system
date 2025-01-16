# Performance Review Workflow

## Stages
1. **Pending Review**: Employee is flagged for performance review.
2. **Review Scheduled**: A review meeting has been scheduled.
3. **Feedback Provided**: Feedback from the review meeting has been documented.
4. **Under Approval**: Feedback is under managerial review.
5. **Review Approved**: Performance review is finalized and approved.
6. **Review Rejected**: Feedback is rejected and requires rework.

## Transitions
- **Pending Review → Review Scheduled**: Triggered when the review date is confirmed.
- **Review Scheduled → Feedback Provided**: Triggered when feedback is recorded after the review meeting.
- **Feedback Provided → Under Approval**: Triggered when feedback is submitted for managerial review.
- **Under Approval → Review Approved**: Triggered when the manager approves the feedback.
- **Under Approval → Review Rejected**: Triggered when the manager rejects the feedback.
- **Review Rejected → Feedback Provided**: Triggered when the feedback is updated after rejection.

## Permissions
- **Manager**: Can schedule reviews, record feedback, and submit for approval.
- **Admin**: Can approve or reject feedback.