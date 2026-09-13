export interface Priority {
  id: number
  name: string
  code: string
}

export interface Status {
  id: number
  name: string
  code: string
}

export interface Task {
  id: number
  title: string
  description: string | null
  deadline: string | null
  status_id: number | null
  priority_id: number | null
  created_at: string
  updated_at: string
}

export interface Pagination<T> {
  items: T[]
  page: number
  per_page: number
  total: number
}

export interface SelectOption {
  label: string
  value: number
}

export interface TaskCreatePayload {
  title: string
  description?: string | null
  deadline?: string | null
  status_id?: number | null
  priority_id?: number | null
}

export type TaskUpdatePayload = Partial<TaskCreatePayload>
