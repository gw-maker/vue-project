import VueRouter from 'vue-router'
import AddBlog from './components/addBlog'
import ListBlog from './components/ListBlog'
import HomeBlog from './components/HomeBlog'
import logBlog from './components/logBlog'
// import up from './components/up'
// import table from './components/table'
// 1、创建路由对象
var router = new VueRouter({
  routes: [
    {path: '/listBlog', component: ListBlog},
    {path: '/addBlog', component: AddBlog},
    {path: '/logBlog', component: logBlog},
    {path: '/', component: HomeBlog}
  ]
})

// 2、把路由对象暴露出去
export default router
