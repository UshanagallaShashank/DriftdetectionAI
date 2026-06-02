// Shared TypeScript types for the DriftdetectionAI frontend
export interface BehaviorRecord {
  id: string
  system_id: string
  session_id?: string
  timestamp: string
  action_type: string
  input_data: Record<string, unknown>
  output_data: Record<string, unknown>
  metadata?: Record<string, unknown>
}

export interface IngestResponse {
  behavior_id: string
  status: string
}

export interface DriftReport {
  id: string
  system_id: string
  analyzed_at: string
  behavior_count: number
  drift_detected: boolean
  confidence: number
  summary: string
  anomalies: string[]
}
