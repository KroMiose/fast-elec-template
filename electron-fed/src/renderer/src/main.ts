import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router/' // 导入路由

import 'virtual:uno.css'

const app = createApp(App)
// 配置路由
app.use(router)

app.mount('#app').$nextTick(() => {
  postMessage({ payload: 'removeLoading' }, '*')
})
