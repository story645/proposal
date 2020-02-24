participants: Tom, Hannah

# What Tom thinks we are on the hook for

 - burning down open issues and open PRs
 - design documents for new data model + artists
 - prototypes for domain specific APIs using said data model + artists
 - new contributor on-boarding

# What we said in the grant:
 Continuous:

- reviewing Issues and Pull Requests, community support, new contributor on-boarding 
- bring resolve rate of new Issues and PRs (# resolved/# open) up to 90% per month
- Reduce backlog open PRs by 50 / quarter
- Reduce backlog of issues by 100 / quarter

Q1: 

- Develop consistent system for labels
- Label 50% of old Issues and PRs
- Start dialog with downstream libraries
    - collect user stories of plotting needs
- Review of architecture of other plotting packages, ready for submission to journal
- Start to identify the categories of `DataSource`s and `Artist`s and their relationships

Q2:

- Label 100% of old Issues and PRs
- Work out API between `Artist` and `DataSource`
- Build a `DataSource` and `Artist` pair Minimal Viable Product with downstream partner

Q3:

- Prototype a high-level API with downstream partner

Q4:

- Finalize end-to-end prototype
- Write white paper and road map
- Journal paper on architecture

# What we've already started on: <- Matplotlib Project board>
* new contributor improvements:
    * easier builds on windows + docker
    * discourse contribute section
* in progress 


# Things to decide today
 - tasks for Tom and Hannah for Nov / Dec

# Tasks
 - put CZI on call agenda for next week
    - we want to make sure we keep community buy in
    - work as open as possible
    - make sure the paid people don't get to do "all the fun stuff"
- create project/multiple projects on CZI stuff
    - maintainance backlog
        - working on
        - needs feedback from post?
        - needs consultations/no path forward 
    - API design

# Expectations for hire:
* participate in weekly developer calls
* other side meetings (weekly checkins)
* remain a member of community in good standing

# haskel vs python implemenations
 - do we want to build them is parallel or serial?
    * inductive - plots + what has to happen to make those examples (prototype
    * deductive - what does the flow look like for a fully functional flow 
* haskell writing out artist tree/scene graph -> serializable form 
    * SVG/Collada/ETC
* internal backend API is svg

# time breakdowns
 - Tom
   - 1 day with SWE / issue work
   - 1 day with Hannah on API / review / ...