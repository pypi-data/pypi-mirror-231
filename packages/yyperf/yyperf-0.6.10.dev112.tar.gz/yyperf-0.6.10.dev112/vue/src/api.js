import request from './request'

export function getDeviceList(params) {
    return request({
        url: '/api/v1/devices/list', method: 'get', params: params
    })
}

export function getPackageList(device) {
    return request({
        url: '/api/v1/devices/' + device + '/packagelist', method: 'get', params: {}
    })
}

export function startAPP(data) {
    return request({
        url: '/api/v1/devices/app', method: 'post', data
    })
}

export function SyncTask(params) {
    return request({
        url: '/task/sync', method: 'get', params: params
    })
}

export function GetCaseInfo(id) {
    return request({
        url: '/case/' + id, method: 'get',
    })
}

export function getMetaFileList(params) {
    return request({
        url: '/file/meta/list', method: 'get', params: params
    })
}

export function installApp(data) {
    return request({
        url: '/api/v1/devices/install', method: 'post', data
    })
}

export function getPerfDataList(params) {
    return request({
        url: '/api/v1/data', method: 'get', params: params
    })
}

export function newPerfRecord(data) {
    return request({
        url: '/api/v1/data', method: 'post', data
    })
}

export function deletePerfRecord(id) {
    return request({
        url: '/api/v1/data/' + id, method: 'delete'
    })
}

export function updatePerfRecord(id, data) {
    return request({
        url: '/api/v1/data/' + id, method: 'patch', data
    })
}