function getSong() {



	var data = document.getElementById("data").value.trim()
	var e = document.getElementById("av");
	var av = e.options[e.selectedIndex].value;
	if(data==""){
		Swal.fire({
			type: 'error',
			animation:false,
			title: data,
			text: 'No input given',
			footer: 'Please give a valid youtube URL',
			backdrop: `rgba(0.090, 0.082, 0.098, 1)`});

	}else{
	Swal.fire({title:'Fetching information...',
	showCancelButton: false,
	showConfirmButton: false,
})
Swal.showLoading()

	eel.get_info(data,av)(status)

	
	
	}
}

function status(data) {
	if(data=='Error!'){
		Swal.fire({
			type: 'error',
			title: data,
			text: 'Something went wrong!',
			footer: 'Please check the URL or network conection',
			backdrop: `rgba(0.090, 0.082, 0.098, 1)`});
	}
	else{
		title=data['title']
		thumb=data['thumb']
		av=data['av']
		url=data['url']

			const swalWithBootstrapButtons = Swal.mixin({
				customClass: {
				  confirmButton: 'btn btn-success',
				  cancelButton: 'btn btn-danger'
				},
				buttonsStyling: false,
			  })
			  
			  swalWithBootstrapButtons.fire({
				title: title,
				input: 'select',
  inputOptions: {
    '1': '',
    '2': '',
    '3': ''
  },
				text: "Do you want to initiate the download?",
				imageUrl: thumb,
				type: 'warning',
				showCancelButton: true,
				confirmButtonText: 'Yes, Download',
				cancelButtonText: 'No, cancel!',

			  }).then((result) => {
				if (result.value) {
		
					const swalWithBootstrapButtons = Swal.mixin({
						customClass: {
						  confirmButton: 'btn btn-success',
						  cancelButton: 'btn btn-danger'
						},
						buttonsStyling: false,
					  })
					  
					  swalWithBootstrapButtons.fire({
						title: title,
						text: "Please wait while downloading.....",
						imageUrl: thumb,
						/*showCancelButton: true,
						showConfirmButton: false,
						cancelButtonText: 'Stop Download',*/
						width: 340,
						padding: '3em',
						backdrop: `rgba(0,0,0,1)url("img/giphy.gif")center left no-repeat`,
					  }).then((result) => {
						if (result.value) {
						} else if (
						  // Read more about handling dismissals
						  result.dismiss === Swal.DismissReason.cancel
						) {	
						//Some  stopper function shoud go here..

						  swalWithBootstrapButtons.fire(
							'Cancelled',
							'Download Cancelled',
							'error'
						  )
						}
					  })

					eel.download(url,av)(response)	
				} else if (
				  
				  result.dismiss === Swal.DismissReason.cancel
				) {
				  swalWithBootstrapButtons.fire(
					'Cancelled',
					'Download Cancelled',
					'error'
				  )
				}
			  })
		  
	}
}


function response(data) {
	if(data=='Error!'){
		Swal.fire({
			type: 'error',
			animation:false,
			title: data,
			text: 'Something went wrong!',
			footer: 'Please check the URL or network conection',
			backdrop: `rgba(0.090, 0.082, 0.098, 1)`});
	}
	else{
		title=data['title'];
		path="To: "+data['path'];
		thumb=data['thumb']
		Swal.fire(
			title+' downloaded',
			path,
			'success')
	}
}





