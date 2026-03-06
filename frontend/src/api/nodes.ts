import apiClient from './client'

export interface Node {
  id: string
  name: string
  url: string
  enabled: boolean
  use_for_auth: boolean
  use_for_chat: boolean
  success: number
  fail: number
  created_at: string
  updated_at: string
}

export interface CreateNodeRequest {
  name: string
  url: string
  use_for_auth?: boolean
  use_for_chat?: boolean
  enabled?: boolean
}

export interface UpdateNodeRequest {
  name?: string
  url?: string
  use_for_auth?: boolean
  use_for_chat?: boolean
  enabled?: boolean
}

export interface ImportUrlsRequest {
  text: string
  use_for_auth?: boolean
  use_for_chat?: boolean
}

export interface ImportClashRequest {
  yaml: string
  local_proxy_port?: number
  use_for_auth?: boolean
  use_for_chat?: boolean
}

export const nodesApi = {
  list: () =>
    apiClient.get<never, { nodes: Node[] }>('/admin/nodes'),

  create: (data: CreateNodeRequest) =>
    apiClient.post<never, Node>('/admin/nodes', data),

  update: (id: string, data: UpdateNodeRequest) =>
    apiClient.put<never, Node>(`/admin/nodes/${id}`, data),

  delete: (id: string) =>
    apiClient.delete(`/admin/nodes/${id}`),

  resetStats: (id: string) =>
    apiClient.post<never, Node>(`/admin/nodes/${id}/reset-stats`, {}),

  importUrls: (data: ImportUrlsRequest) =>
    apiClient.post<never, { imported: number; nodes: Node[] }>('/admin/nodes/import/urls', data),

  importClash: (data: ImportClashRequest) =>
    apiClient.post<never, { imported: number; nodes: Node[] }>('/admin/nodes/import/clash', data),
}
