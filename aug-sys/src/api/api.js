// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance
const ip = 'http://127.0.0.1:8000/api/'

const datasetUrl = ip + 'dataset'
const getModelUrl = ip + 'getModel'
const deleteModelUrl = ip + 'deleteModel'
const downloadModelUrl = ip + 'downloadModel'
const deleteDataUrl = ip + 'deleteDataset'
const deepTaskUrl = ip + 'deepTask'
const segTaskUrl = ip + 'segTask'
const taskUrl = ip + 'getTask'
const deleteAugTaskUrl = ip + 'deleteAugTask'
const getAugDetailUrl = ip + 'getAugDetail'
const instanceListUrl = ip + 'getInstance'
export const getDatasetDetail = () => {
  return axios.get(datasetUrl)
}
export const getModel = () => {
  return axios.get(getModelUrl)
}
export const deleteModel = (parms) => {
  return axios.post(deleteModelUrl, parms)
}
export const downloadModel = (parms) => {
  return axios.post(downloadModelUrl, parms)
}
export const deleteDataset = (parms) => {
  return axios.post(deleteDataUrl, parms)
}
export const deepTask = (parms) => {
  return axios.post(deepTaskUrl, parms)
}
export const segTask = (parms) => {
  return axios.post(segTaskUrl, parms)
}
export const showMessage = (parms) => {
  this.$message({
    message: parms.message,
    type: parms.type
  })
}
export const getTask = () => {
  return axios.get(taskUrl)
}
export const deleteAugTask = (parms) => {
  return axios.post(deleteAugTaskUrl, parms)
}
export const getAugDetail = (parms) => {
  return axios.post(getAugDetailUrl, parms)
}
export const getInstance = () => {
  return axios.get(instanceListUrl)
}
