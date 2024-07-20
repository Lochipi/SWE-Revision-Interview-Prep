## **Replication** 
Replication means keeping a copy of the same data on multiple machines that are
connected via a network.

there are several reasons why you might want to replicate data:
- • To keep data geographically close to your users (and thus reduce latency)
- • To allow the system to continue working even if some of its parts have failed
(and thus increase availability)
- • To scale out the number of machines that can serve read queries (and thus
increase read throughput)

If the data you're replicating remains static, replication is straightforward: simply copy the data to each node once, and the task is complete. The real challenge in replication arises when managing changes to the replicated data.

### popular algorithms for replicating changes to data:
- single-leader
- multi-leader
- leaderless replication

Almost all distributed databases use one of these three approaches. They all have various pros and cons, which we will examine in detail in the later series.


#### Leaders and Followers
Each node that stores a copy of the database is called a *`replica`*.

Every write to the database needs to be processed by every **replica**; otherwise, the *replicas* would no longer contain the same data. The most common solution for this is called *leader-based replication* (also known as *active/passive* or *master–slave replication*)

Here's how it works:
1. One of the replicas is designated the leader (also known as master or primary).
When clients want to write to the database, they must send their requests to the
leader, which first writes the new data to its local storage.
2. The other replicas are known as followers (read replicas, slaves, secondaries, or hot
standbys). Whenever the leader writes new data to its local storage, it also sends
the data change to all of its followers as part of a replication log or change stream.
Each follower takes the log from the leader and updates its local copy of the data‐
base accordingly, by applying all writes in the same order as they were processed
on the leader.
3. When a client wants to read from the database, it can query either the *leader* or any of the followers. However, *writes* are only accepted on the *leader* (the followers are *read-only* from the client’s point of view).

![image](https://github.com/Lochipi/SWE-Revision-Interview-Prep/assets/108942025/dc0491af-4056-4c63-ae31-fc493af1b423)
You can [view it using this link](https://drive.google.com/file/d/1-_c7BPgJdn80gNY98HxGMWoRB3_mp6WD/view?usp=sharing) 

incase the image above is not found.

This mode of replication is a built-in feature of many relational databases, such as 
- **MySQL**, 
- **PostgreSQL**, 
- **SQL Server’s AlwaysOn Availability Groups** 
- and **Oracle Database**, 

as well as some **NoSQL** databases, such as 
- **MongoDB**  
- **RethinkDB**
- **Espresso**

These are the things you shuold note. Remember that, leader-based replication is not restricted to only databases. It is also used in other distributed messages systems, such as **Kafka** and **RabbitMQ** which you can use them too.

that's it for today! will update on the above example using an image demonstrating more of how it works. Stay tuned! 🌟
