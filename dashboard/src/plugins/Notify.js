import Notification from '@/components/Notification'

import { events } from '@/utils/event'

const NotifyPlugin = {

  install (Vue, options) {
    Vue.component('notifications', Notification)

    const notify = (message) => {
        events.$emit('add', message)
    }

    Vue.prototype.$notify = notify
    Vue.notify = notify

  }
}


export default NotifyPlugin
