# Remote Repositories

The **Remote Repositories extension** integrates with the GitHub Repositories and Azure Repos extensions, allowing you to quickly browse, search, edit, and commit to remote git repositories directly from within Visual Studio Code.

This extension was previously part of the GitHub Repositories extension.

## Trust when reviewing pull requests

Trust in a base repository does not imply trust in a fork that submits a pull request. GitHub Repositories identifies the source repository, and Remote Repositories reports that source through the canonical-URI provider. VS Code checks workspace trust against the source before enabling trust-dependent extensions.

For an untrusted fork, the trust prompt names the source repository. Choose **Cancel** to keep reviewing in Restricted Mode, or **Trust Folder & Continue** to approve that fork separately. Restricted Mode still permits reading files and applying non-restricted settings, such as a color theme.

If the source cannot be determined, the workspace remains restricted and cannot be approved as though it came from the base repository. Open **Manage Workspace Trust**, sign in or enable the repository extension if needed, and select **Retry Source Check**. A successful retry restores the normal trust decision; it does not approve an untrusted source.

Source lookups time out after 30 seconds so a stalled provider cannot block later trust actions indefinitely. Cancellation lets **Retry Source Check** start a fresh metadata lookup without cancelling other callers. Late responses cannot replace the retry's cached metadata. Restarting an extension host retains an already-verified source; the source is checked again when the provider registers in the new host.

GitHub Enterprise trust includes the server address. Previous approvals that did not identify a server must be granted again; they cannot safely be reused across different enterprise servers. Providers that do not report verified PR source information, including the current Azure Repos provider, leave PR workspaces restricted instead of falling back to base-repository trust. Normal branches and tags still resolve to their repository.

This behavior requires the coordinated VS Code workspace-trust change that resolves virtual resources through the canonical-URI provider. Remote Repositories alone cannot enforce the startup boundary on an older VS Code version. Restricted Mode is not a network sandbox and does not prevent every download or every extension from running.

The coordinated core change also applies extension trust requirements to browser-only entry points. Browser-only extensions must declare support for untrusted workspaces to run in Restricted Mode, just like extensions with a desktop entry point. Declarative extensions, such as themes with no executable entry point, remain available.
