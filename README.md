## Work (very much) In Progress

The end-goal is to have a website display realtime info about resources running in the same cluster.

* __watcher__: Requests from kubernetes API and publishes podList events to RethinkDB
* __db__: Holds an events table
* __front__: Subscribes to RethinkDB, displays in realtime events from db
