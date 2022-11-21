import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import segtest from '@/components/segtest'
import deeptest from '@/components/deeptest'
import dataset from '@/components/dataset'
import model from '@/components/model'
import augList from '@/components/augList'
import instanceList from '@/components/instanceList'
import augTaskDetail from '@/components/augTaskDetail'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/segtest',
      name: 'segtest',
      component: segtest
    },
    {
      path: '/deeptest',
      name: 'deeptest',
      component: deeptest
    },
    {
      path: '/dataset',
      name: 'dataset',
      component: dataset
    },
    {
      path: '/model',
      name: 'model',
      component: model
    },
    {
      path: '/augList',
      name: 'augList',
      component: augList
    },
    {
      path: '/instanceList',
      name: 'instanceList',
      component: instanceList
    },
    {
      path: '/augTaskDetail',
      name: 'augTaskDetail',
      component: augTaskDetail
    }
  ]
})
