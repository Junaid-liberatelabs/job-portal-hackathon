from pydantic import BaseModel
from typing import List, Optional


class CareerRoadmapRequest(BaseModel):
    timeframe: str
    available_learning_time: str


class GraphNode(BaseModel):
    id: str
    label: str
    type: str
    description: Optional[str] = None
    metadata: Optional[dict] = None


class GraphEdge(BaseModel):
    source: str
    target: str
    label: Optional[str] = None
    type: Optional[str] = None


class CareerRoadmapGraphData(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]


class CareerRoadmapResponse(BaseModel):
    career_roadmap_report: str
    graph_data: Optional[CareerRoadmapGraphData] = None