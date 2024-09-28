import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from '../router/index' // 导入路由

import 'virtual:uno.css'

const app = createApp(App)
app.use(router) // 使用路由
app.mount('#app')
