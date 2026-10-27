#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WH_CONVERGENCE_AUDIT_ENGINE
Protocol: WH-IMPLEMENTATION-TRACE-2026-10-26
Purpose: Validates that visual artifacts accurately represent the logical pipeline.
"""

class ConvergenceAuditEngine:
    def __init__(self):
        self.current_state = "UNVERIFIED_MANIFEST"
        self.metrics = {
            "IMAGE_TO_PROCESS_RATIO": None,
            "CONVERGING_PROCESS_SYMMETRY_INDEX": None
        }
        self.evidence = {}

    def evaluate_symmetry(
        self,
        pipeline_nodes,
        diagram_assets,
        pipeline_edges,
        diagram_edges,
        manifest_validated=False
    ):
        # A valid manifest and complete inputs are prerequisites.
        if not manifest_validated:
            return self._unverified("MANIFEST_NOT_VALIDATED")

        if not all((
            pipeline_nodes,
            diagram_assets is not None,
            pipeline_edges is not None,
            diagram_edges is not None
        )):
            return self._unverified("INCOMPLETE_INPUTS")

        nodes = set(pipeline_nodes)

        # Each visual asset must identify its corresponding process node.
        mapped = [
            asset.get("node_id")
            for asset in diagram_assets
            if isinstance(asset, dict)
            and asset.get("node_id") is not None
        ]

        if len(mapped) != len(set(mapped)):
            return self._unverified("DUPLICATE_NODE_MAPPING")

        if not set(mapped).issubset(nodes):
            return self._unverified("UNKNOWN_NODE_MAPPING")

        visual_nodes = set(mapped)
        node_coverage = len(visual_nodes) / len(nodes)

        process_edges = set(map(tuple, pipeline_edges))
        visual_edges = set(map(tuple, diagram_edges))

        # Reject edges that reference nodes absent from the pipeline.
        if any(
            len(edge) != 2
            or edge[0] not in nodes
            or edge[1] not in nodes
            for edge in process_edges | visual_edges
        ):
            return self._unverified("INVALID_EDGE_REFERENCE")

        # Every visual dependency must correspond to a real dependency.
        if not visual_edges.issubset(process_edges):
            return self._unverified("UNSUPPORTED_VISUAL_EDGE")

        if process_edges:
            edge_coverage = (
                len(visual_edges & process_edges)
                / len(process_edges)
            )
        else:
            edge_coverage = 1.0 if not visual_edges else 0.0

        symmetry_index = (
            0.5 * node_coverage
            + 0.5 * edge_coverage
        )

        self.metrics = {
            "IMAGE_TO_PROCESS_RATIO": node_coverage,
            "CONVERGING_PROCESS_SYMMETRY_INDEX": symmetry_index
        }

        self.evidence = {
            "node_coverage": node_coverage,
            "edge_coverage": edge_coverage,
            "unmapped_nodes": sorted(nodes - visual_nodes),
            "unrepresented_edges": sorted(
                process_edges - visual_edges
            )
        }

        if node_coverage == 1.0 and edge_coverage == 1.0:
            self.current_state = "CANONICAL_CONVERGENCE"
        elif symmetry_index >= 0.8:
            self.current_state = "STRUCTURALLY_ALIGNED"
        else:
            self.current_state = "ASYMMETRIC_DRIFT"

        return self.current_state

    def _unverified(self, reason):
        self.current_state = "UNVERIFIED_MANIFEST"
        self.metrics = {
            "IMAGE_TO_PROCESS_RATIO": None,
            "CONVERGING_PROCESS_SYMMETRY_INDEX": None
        }
        self.evidence = {"reason": reason}
        return self.current_state

    def get_audit_report(self):
        return {
            "framework":
                "WH_SYMMETRY_CONVERGENCE_AUDIT_FRAMEWORK",
            "evaluation_state": self.current_state,
            "recorded_metrics": self.metrics,
            "evidence": self.evidence
        }
