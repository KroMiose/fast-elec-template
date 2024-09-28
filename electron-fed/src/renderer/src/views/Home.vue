// src/renderer/src/views/Home.vue

<template>
  <div>
    <h1>Home Page</h1>
    <button @click="fetchData">Fetch Data</button>
    <p v-if="loading">Loading...</p>
    <p v-if="error">Error: {{ error }}</p>
    <pre v-if="data">{{ data }}</pre>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { get } from '../utils/axios' // 导入 get 函数

// 假设你的 API 返回的数据类型
interface UserData {
  id: number
  name: string
  email: string
}

export default defineComponent({
  setup() {
    const data = ref<UserData | null>(null)
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchData = async () => {
      loading.value = true
      error.value = null
      try {
        // 调用 get 函数发送请求
        const response = await get<UserData>('/health') // 假设 API 路径为 /users/1
        data.value = response
      } catch (err: any) {
        error.value = err.message || 'Something went wrong'
      } finally {
        loading.value = false
      }
    }

    return { data, loading, error, fetchData }
  }
})
</script>
