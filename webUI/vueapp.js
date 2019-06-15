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
    sendOnRequestAjax: function () {
      var vm = this
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
          if (this.status == 200) {
            vm.toggle();
            vm.outmessage = "Success!"
          } else {
            vm.outmessage = "Error!"
          }
        }
      }
      xhttp.open("GET", "ajax_response.txt", true);
      xhttp.send();
    },
    sendOnRequest: function () {
      vm = this
      this.outmessage = "Connecting..."
      axios.get('https://yesno.wtf/api')
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
  