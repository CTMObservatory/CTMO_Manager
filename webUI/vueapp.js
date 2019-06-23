Vue.component('single-switch', {
  props: ['ipaddress', 'label'],
  template: `
  <div>
    <label class="switch">
      <input type="checkbox" :checked="state" v-on:click="toggle">
      <span class="slider round"></span>
    </label>
    <label>{{ label }} is {{ state ? "ON": "OFF" }}</label>
    <p>Will connect to {{ ipaddress }}</p>
    <p>{{ outmessage }}</p>
  </div>
  `,
  data: function() {
    return {
      state: false,
      outmessage: ""
    }
  },
  methods: {
    toggle: function() {
      this.state = !this.state
      this.sendOnRequest()
    },
    sendOnRequest: function () {
      vm = this
      this.outmessage = "Connecting..."
      wo_on = `<?xml version='1.0'?>
<methodCall>
    <methodName>front_desk</methodName>
    <params>
        <param>
            <value><struct>
                <member>
                    <name>ID</name>
                    <value><string>1</string></value>
                </member>
                <member>
                    <name>WOType</name>
                    <value><string>Dome</string></value>
                </member>
                <member>
                    <name>Priority</name>
                    <value><int>2</int></value>
                </member>
                <member>
                    <name>Datetime</name>
                    <value><string>2019-03-05T14:34:54.234</string></value>
                </member>
                <member>
                    <name>User</name>
                    <value><string>John Doe</string></value>
                </member>
                <member>
                    <name>Blink01</name>
                    <value><boolean>1</boolean></value>
                </member>
            </struct></value>
        </param>
    </params>
</methodCall>`
      wo_off = `<?xml version='1.0'?>
<methodCall>
    <methodName>front_desk</methodName>
    <params>
        <param>
            <value><struct>
                <member>
                    <name>ID</name>
                    <value><string>1</string></value>
                </member>
                <member>
                    <name>WOType</name>
                    <value><string>Dome</string></value>
                </member>
                <member>
                    <name>Priority</name>
                    <value><int>2</int></value>
                </member>
                <member>
                    <name>Datetime</name>
                    <value><string>2019-03-05T14:34:54.234</string></value>
                </member>
                <member>
                    <name>User</name>
                    <value><string>John Doe</string></value>
                </member>
                <member>
                    <name>Blink01</name>
                    <value><boolean>0</boolean></value>
                </member>
            </struct></value>
        </param>
    </params>
</methodCall>`
      if (this.state) {
        wo = wo_on
      } else {
        wo = wo_off
      }
      axios({
        method: 'post',
        url: this.ipaddress,
        data: wo,
        headers: {
          'Content-type': 'text/xml'
        }
      })
      //axios.post(url, {'Content-type': 'text/xml'})
      .then(function (response) {
        vm.outmessage = "Success!"
        console.log(response.data)
      })
      .catch(function (error) {
        vm.outmessage = 'Error! '
        console.log(error)
      })
    }
  }
});

var switchapp = new Vue({
  el: "#switchapp",
  data: function () {
    return {
      address: ""
    }
  }
})
  