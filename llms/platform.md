# Bounded context: Platform

Models the platform-wide objects that other bounded contexts build on: organizations (Company Accounts) with their users and user groups, Workspaces with their members and groups, applications, event subscriptions, and Renesas 365 solutions with their releases. It also holds the lifecycle definitions (with their stages and states) and revision naming schemes that govern Workspace Items. Organization-level data is managed in the Company Dashboard; Workspace-level configuration, including these definitions and schemes, is managed from Altium Designer or the Workspace browser interface.

HTML page: [subsets/platform/](../subsets/platform/)

## In the product

- [Company Dashboard](https://www.altium.com/documentation/altium-dashboard) (primary)
- [Configuring and Administrating Your Workspace](https://www.altium.com/documentation/altium-designer/connected-workspace)
- [Altium 365 API](https://www.altium.com/documentation/altium-developer-center/altium-365/api#how_the_api_is_organized)

## Classes

- [Application](classes/plt_Application.md) (`plt_Application`): Artifact · API GloApp · GRID `grid:global::platform:application/{id}`
- [Event Subscription](classes/plt_EventSubscription.md) (`plt_EventSubscription`): Artifact · API GloEvtSubscription · GRID `grid:global::events:subscription/{id}`
- [Lifecycle Definition](classes/plt_LifecycleDefinition.md) (`plt_LifecycleDefinition`): Defines the set of states that an entity can transition through in its lifecycle. · Artifact · API DesLifeCycleDefinition · GRID `grid:workspace:{workspace-id}:platform:lifecycle-definition/{id}`
- [Lifecycle Stage](classes/plt_LifecycleStage.md) (`plt_LifecycleStage`): A named stage that groups lifecycle states in a lifecycle definition using the Advanced management style (e.g. Design, Prototype, Production), indicating how far a revision has progressed in its development. · Resource · API DesLifeCycleStage
- [Lifecycle State](classes/plt_LifecycleState.md) (`plt_LifecycleState`): A named point in an Item Revision's lifecycle (e.g. Planned, New From Design, In Production, Obsolete) that shows its status from a business perspective. · Resource · API DesLifeCycleState
- [Organization](classes/plt_Organization.md) (`plt_Organization`): An Altium customer organization, represented by its Company Account. · Artifact · API GloOrganization · GRID `grid:global::platform:organization/{id}`
- [Revision Naming Scheme](classes/plt_NamingScheme.md) (`plt_NamingScheme`): Defines the format of Revision IDs for the Items that use it: one to three levels (e.g. Model, Prototype and Revision), each with its own format, separator and minimum width. · Artifact · API DesRevisionNamingScheme · GRID `grid:workspace:{workspace-id}:platform:revision-naming-scheme/{id}`
- [Solution](classes/plt_Solution.md) (`plt_Solution`): A Renesas 365 solution: the main, top-level object of a Renesas 365 Workspace, which brings together the system design (an ESD document), PCB projects and software projects of one system. · Activity · API SolSolution · GRID `grid:workspace:{workspace-id}:platform:solution/{id}`
- [Solution Release](classes/plt_SolutionRelease.md) (`plt_SolutionRelease`): Release of the Solution. · Artifact · GRID `grid:workspace:{workspace-id}:platform:solution-release/{id}`
- [User](classes/plt_User.md) (`plt_User`): A person identified by a global Altium Account, the identity used for signing in to Altium services. · Artifact · API GloUser · GRID `grid:global::platform:user/{id}`
- [User Group](classes/plt_UserGroup.md) (`plt_UserGroup`): A named group of users within an organization's Company Account, managed in the Company Dashboard. · Artifact · API GloUserGroup · GRID `grid:global::platform:group/{id}`
- [Workspace](classes/plt_Workspace.md) (`plt_Workspace`): The top-level entity that plays a role of a closed environment for other entities (members, projects, components, etc.). · Artifact · API DesWorkspace · GRID `grid:global::platform:workspace/{id}`
- [Workspace Group](classes/plt_WorkspaceGroup.md) (`plt_WorkspaceGroup`): Workspace Group represents a logical collection of users within a workspace, used to manage access control, permissions, and collaboration roles across projects and data assets. · Artifact · API DesWorkspaceGroup · GRID `grid:workspace:{workspace-id}:team:group/{id}`
- [Workspace User](classes/plt_WorkspaceUser.md) (`plt_WorkspaceUser`): A person's membership in a particular Workspace, connecting their Altium Account to that Workspace and to the Workspace groups they are assigned to. · Artifact · API DesWorkspaceUser · GRID `grid:workspace:{workspace-id}:team:user/{id}`

## Base classes and mixins

- [Has Lifecycle](classes/plt_HasLifecycle.md) (`plt_HasLifecycle`): Mixin that adds a lifecycle state reference to an entity. · abstract, mixin
- [Solution Item](classes/plt_SolutionItem.md) (`plt_SolutionItem`): Mixin that marks an entity as an item belonging to a platform Solution. · abstract, mixin
