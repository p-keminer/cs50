# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

Random partitioning prevents the data sets for individual boots from having different sizes or requiring different processing, but individual data must be processed across multiple boots, and the data sets must be assembled.

## Partitioning by Hour

Partitioning by hour simplifies data collection and querying, but individual boats are subject to varying levels of load at specific times

## Partitioning by Hash Value

Partitioning by hash also distributes observations evenly across the nodes, which helps balance storage space and load; however, querying records becomes more difficult if the hash values for a given timestamp are unknown.
