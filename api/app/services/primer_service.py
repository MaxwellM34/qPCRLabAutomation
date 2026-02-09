from app.schemas.primer import PrimerDesignRequest, PrimerDesignResponse, PrimerResult


def design_primers(payload: PrimerDesignRequest) -> PrimerDesignResponse:
    sequence = payload.target_sequence.upper().replace(" ", "").replace("\n", "")
    target_length = len(sequence)

    # Simple placeholder logic for scaffolding:
    # real primer design should include GC%, Tm, hairpin, dimer, and specificity checks.
    forward_primer = sequence[:20]
    reverse_region = sequence[-20:]
    reverse_primer = reverse_region[::-1].translate(str.maketrans("ATCG", "TAGC"))
    amplicon_size = min(max(payload.amplicon_min, 100), payload.amplicon_max)

    return PrimerDesignResponse(
        target_length=target_length,
        result=PrimerResult(
            forward_primer=forward_primer,
            reverse_primer=reverse_primer,
            amplicon_size=amplicon_size,
        ),
    )
