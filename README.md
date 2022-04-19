# OptimizingPublicTransportation

This is a project for the Udacity Nanodegree Data Streaming.

## Current Deviations

- Using version 6.2.2 instead of 5.2.2
- Attempted to add 2 more Brokers but had issues with consuming - will revisit another time

## How to run

Start Kafka and all its components up

```
docker-compose up
```

You will first need to ensure the python libraries are installed.

```
cd producers
```

```
ulimit -n 4096
```

```
pip install -r requirements.txt
```

Run the python simulation - this will start producing data to the topics

```
python3 simulation.py
```

Run the faust application to summarise the station topic

```
cd consumers
```

```
pip install -r requirements.txt
```

```
faust -A faust_stream worker -l info
```

Run the KSQL script to create a summary of the turnstile data

```
cd consumers
```

```
pip install -r requirements.txt
```

```
python3 ksql.py
```

Run the consumers

```
cd consumers
```

```
pip install -r requirements.txt
```

```
python3 server.py
```