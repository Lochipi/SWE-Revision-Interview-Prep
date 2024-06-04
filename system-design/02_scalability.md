# Intro

Welcome to the first guide. It is important to note that the order might be a little different, I would advice you check on the headings to know what you are looking for.

In this guide, we will be looking at the following:
since it is the biginning, we will be looking at these concepts a lot, terminologies of scallability.

## What is Scalability?

Scalability is the ability of a system to handle increased load without impacting performance. If your data volume, read load, or write load grows bigger than a single machine can handle, you can potentially spread the load across multiple machines.

Scalability can be achieved through various means, such as **horizontal scaling** (adding more machines) or **vertical scaling** (upgrading existing machines).

## 1. Scaling to higher loads. - Vertical Scaling

The simplest approach to scaling is to upgrade your existing machine. You can increase the **CPU**, **memory**, **storage**, or **network capacity** of your machine to handle higher loads.

This is fits in the kind of :

### a. shared memory architecture

In a shared memory architecture, multiple processors share the same memory space. This allows for faster communication between processors, but it can also lead to bottlenecks when multiple processors try to access the same memory location.
All the components can be treated as a single machine.

This is the simplest way to scale a system, but it has its limitations. You can only scale as far as the capacity of a single machine allows.

##### bottleneck

the cost grows faster than line‐arly: a machine with twice as many CPUs, twice as much RAM, and twice as much disk capacity as another typically costs significantly more than twice as much.
And due to bottlenecks, a machine twice the size cannot necessarily handle twice the load.

A **shared-memory architecture** may offer limited fault tolerance—high-end machines
have hot-swappable components (you can replace disks, memory modules, and even
CPUs without shutting down the machines)—but it is definitely limited to a single
geographic location.

### b. shared disk architecture

In a shared disk architecture, multiple machines share the same disk storage. The machines can read and write data to the same disk, allowing for better fault tolerance and data redundancy.
This machines often have independent memory and CPUs, but they share the same disk storage.
This allows for better **fault tolerance** and **data redundancy**, but it can also lead to bottlenecks when multiple machines try to access the same disk.

This architecture is used for some data warehousing workloads, but contention and the overhead of lock‐ing limit the scalability of the shared-disk approach.

### 2. shared nothing architecture - Horizontal Scaling

This is the most common way to scale a system. In a shared-nothing architecture, each machine operates independently and does not share memory or disk storage with other machines.

**node** - a single machine in a distributed system,physical or virtual
machine running the database software. Each node uses its CPUs,
RAM, and disks independently

**cluster** - a group of nodes that work together to store and serve data. Clusters can be used to increase the capacity and fault tolerance of a system.

Any coordination between nodes is done at the software level, using a **conventional network**(usually TCP/IP) to communicate.

No special hardware is required by a shared-nothing system, so you can use whatever
machines have the best price/performance ratio. You can potentially distribute data
across multiple geographic regions, and thus reduce latency for users and potentially be able to survive the loss of an entire datacenter.

The shared nothing architecture is neccessarily the best choice for every use case, and the most cautiion from you, the application developer.

## Note:

In some cases, a simple single-threaded program can perform significantly better than a cluster with over 100 CPU cores. HOw is this so? The single-threaded program can keep all its data in RAM, while the cluster must store data on disk, which is much slower than RAM.

In a large machine, although any CPU can access any part of memory, some banks of memory are closer to one CPU than to others (this is called nonuniform memory access, or NUMA). To make efficient use of this architecture, the processing needs to be broken down so that each CPU mostly accesses memory that is nearby—which means that partitioning is still required, even when ostensibly running on one machine.
