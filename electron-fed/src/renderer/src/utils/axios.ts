import axios, { AxiosResponse, AxiosError, InternalAxiosRequestConfig, AxiosHeaders } from 'axios'

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8866/api', // 设置 API 基础 URL
  timeout: 5000 // 设置请求超时时间
  // 其他配置项，例如 headers, withCredentials 等
})

// 请求拦截器
instance.interceptors.request.use(
  (
    config: InternalAxiosRequestConfig
  ): InternalAxiosRequestConfig | Promise<InternalAxiosRequestConfig> => {
    const token = localStorage.getItem('token') // 获取 token
    if (token) {
      if (!config.headers) {
        config.headers = new AxiosHeaders() // 确保 headers 不为空
      }
      ;(config.headers as AxiosHeaders).set('Authorization', `Bearer ${token}`) // 使用 set 方法来添加 Authorization
    }
    return config
  },
  (error: AxiosError) => {
    console.error('请求错误:', error)
    return Promise.reject(error) // 返回错误，以便在调用处捕获
  }
)

// 响应拦截器
instance.interceptors.response.use(
  (response: AxiosResponse) => {
    // 对响应数据做些什么
    const data = response.data
    if (data.code === 200) {
      // 假设 API 返回 code 为 200 表示成功
      return data.data // 只返回 data 部分
    } else {
      // 处理错误情况，例如显示错误信息
      console.error('API 错误:', data.message)
      return Promise.reject(data) // 或者返回一个自定义的错误对象
    }
  },
  (error: AxiosError) => {
    // 对响应错误做些什么
    console.error('响应错误:', error)
    // 可以根据错误状态码进行不同的处理
    if (error.response) {
      switch (error.response.status) {
        case 401: // 未授权
          // 跳转到登录页面
          break
        case 403: // 禁止访问
          // 显示错误信息
          break
        case 404: // 资源未找到
          // 显示错误信息
          break
        default:
          // 显示通用错误信息
          break
      }
    } else if (error.request) {
      // 请求已发送，但没有收到响应
      console.error('请求超时')
    } else {
      // 其他错误
      console.error('其他错误:', error.message)
    }
    return Promise.reject(error)
  }
)

// 定义泛型接口，用于描述 API 返回数据的结构
interface ApiResponse<T> {
  code: number
  message: string
  data: T
}

// GET 请求
export const get = <T>(url: string, params?: unknown): Promise<T> => {
  return instance.get<ApiResponse<T>>(url, { params }).then((response) => {
    if (response.data.code === 200) {
      return response.data.data
    } else {
      console.error('API 错误:', response.data.message)
      return Promise.reject(response.data)
    }
  })
}

// POST 请求
export const post = <T>(url: string, data?: unknown): Promise<T> => {
  return instance.post<ApiResponse<T>>(url, data).then((response) => {
    if (response.data.code === 200) {
      return response.data.data
    } else {
      console.error('API 错误:', response.data.message)
      return Promise.reject(response.data)
    }
  })
}

// PUT 请求
export const put = <T>(url: string, data?: unknown): Promise<T> => {
  return instance.put<ApiResponse<T>>(url, data).then((response) => {
    if (response.data.code === 200) {
      return response.data.data
    } else {
      console.error('API 错误:', response.data.message)
      return Promise.reject(response.data)
    }
  })
}

// DELETE 请求
export const del = <T>(url: string, params?: unknown): Promise<T> => {
  return instance.delete<ApiResponse<T>>(url, { params }).then((response) => {
    if (response.data.code === 200) {
      return response.data.data
    } else {
      console.error('API 错误:', response.data.message)
      return Promise.reject(response.data)
    }
  })
}

export default instance
