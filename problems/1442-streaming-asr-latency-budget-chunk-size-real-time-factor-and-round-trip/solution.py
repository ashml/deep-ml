import math


def chunk_latency(chunk_s, rtf, rtt_s):
    return chunk_s + rtf * chunk_s + rtt_s


def largest_chunk_under(budget_s, rtf, rtt_s, step=0.05):
    size = 0
    while (size + step) * (1 + rtf) + rtt_s <= budget_s + 1e-12:
        size += step
    return None if size == 0 else round(size, 2)


def concurrent_streams(rtf, gpu_share=1.0):
    return math.floor(gpu_share / rtf)


def end_of_speech_latency(hangover_s, chunk_s, rtf, rtt_s):
    return hangover_s + chunk_latency(chunk_s, rtf, rtt_s)


def budget_breakdown(chunk_s, rtf, rtt_s):
    total = chunk_latency(chunk_s, rtf, rtt_s)

    return {
        "wait": round(chunk_s / total, 4),
        "model": round(rtf * chunk_s / total, 4),
        "network": round(rtt_s / total, 4),
    }
