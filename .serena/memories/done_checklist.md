# When a task is completed
- Run the relevant just recipe(s); proof auditing requires scripts to run via just and exit 0.
- Verify assertions have external sources and fraud indicators are absent.
- Check git diff immediately after edits.
- Ensure task artifacts required by STATE_MACHINE.md are present and current.
- Confirm scope isolation and no collateral diff outside scope.yml.
- For theorem/conjecture promotion, ensure replay transcript, attack bundle, and acceptance bundle completeness before treating output as trusted.
