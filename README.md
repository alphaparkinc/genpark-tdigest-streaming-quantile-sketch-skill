# genpark-tdigest-streaming-quantile-sketch-skill

[![CI](https://github.com/alphaparkinc/genpark-tdigest-streaming-quantile-sketch-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/alphaparkinc/genpark-tdigest-streaming-quantile-sketch-skill/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> t-Digest online streaming quantile estimation algorithm clustering centroid clusters for high-precision P99 and P99.9 latency SLAs.

## Architecture

```mermaid
flowchart TD
    Client[AI Agent / Telemetry Source] -->|Trace Context / Span / Metric| Engine[genpark-tdigest-streaming-quantile-sketch-skill]
    Engine --> ObservabilityCore[Tracing Propagator & Histogram Aggregator]
    ObservabilityCore --> Collector[(OpenTelemetry Collector / Dashboard)]
```

## Features
- Pure standard library Python implementation with strictly zero pip dependencies.
- Production-grade telemetry principles (W3C traceparent, HdrHistogram, t-Digest, Dapper sampling).
- Native Model Context Protocol (MCP) server support for AI agent observability.

## Installation

```bash
git clone https://github.com/alphaparkinc/genpark-tdigest-streaming-quantile-sketch-skill.git
cd genpark-tdigest-streaming-quantile-sketch-skill
```

## Quickstart

```bash
python example_usage.py
```
