        document.addEventListener('DOMContentLoaded', () => {
            const dropZone = document.getElementById('dropZone');
            const resultsDiv = document.getElementById('results');
            const classifyBtn = document.getElementById('classifyBtn');
            let currentFile = null;

            dropZone.addEventListener('click', () => {
        
                const fileInput = document.createElement('input');
                fileInput.type = 'file';
                fileInput.accept = 'image/*';
                fileInput.onchange = (e) => handleFiles(e.target.files);
                fileInput.click();
            });

            
            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                dropZone.addEventListener(eventName, preventDefaults, false);
            });

            function preventDefaults(e) {
                e.preventDefault();
                e.stopPropagation();
            }

            ['dragenter', 'dragover'].forEach(eventName => {
                dropZone.addEventListener(eventName, highlight, false);
            });

            ['dragleave', 'drop'].forEach(eventName => {
                dropZone.addEventListener(eventName, unhighlight, false);
            });

            function highlight() {
                dropZone.classList.add('highlight');
            }

            function unhighlight() {
                dropZone.classList.remove('highlight');
            }

            dropZone.addEventListener('drop', (e) => {
                const dt = e.dataTransfer;
                handleFiles(dt.files);
            });

            function handleFiles(files) {
                if (!files.length) return;

                currentFile = files[0];
                classifyBtn.disabled = false;
             
                const reader = new FileReader();
                reader.onload = (e) => {
                    resultsDiv.innerHTML = `
                        <p>Image ready for classification</p>
                        <img src="${e.target.result}" 
                             alt="Uploaded preview" 
                             style="max-width: 300px; margin-top: 1rem;">
                    `;
                    resultsDiv.classList.add('show');
                };
                reader.readAsDataURL(currentFile);
            }

            async function classifyImage() {
                if (!currentFile) return;

                classifyBtn.disabled = true;
                classifyBtn.innerHTML = 'Classifying <span class="loading-spinner"></span>';
                
                try {
            
                    const imageBase64 = await getBase64(currentFile);
                    
                    // Use the API URL from config
                    const response = await fetch(`${CONFIG.API_BASE_URL}/api/classify`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            image_data: imageBase64.split(',')[1] 
                        })
                    });

                    const result = await response.json();

                    if (result.error === "No face detected") {
                        resultsDiv.innerHTML = `
                            <div style="text-align: center;">
                                <h2 style="color: #f44336; margin-bottom: 1rem;">Warning</h2>
                                <p style="font-size: 1.2rem;">Unable to detect a face in the image.</p>
                                <p style="font-size: 1rem;">Please upload an image with a clear face.</p>
                            </div>
                        `;
                    } else {
                    resultsDiv.innerHTML = `
                        <div style="text-align: center;">
                            <h2 style="color: #4CAF50; margin-bottom: 1rem;">Classification Results</h2>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 1.5rem;">
                                <div style="text-align: left;">
                                    <p style="font-size: 1.2rem; margin-bottom: 0.5rem;"><strong>Politician:</strong> ${result.politician_name}</p>
                                    <div style="background: #f1f1f1; border-radius: 20px; height: 10px; width: 100%; margin-bottom: 0.5rem;">
                                        <div style="background: #4CAF50; height: 100%; border-radius: 20px; width: ${result.confidence}%;"></div>
                                    </div>
                                    <p style="font-size: 1rem;"><strong>Confidence:</strong> ${result.confidence}%</p>
                                </div>
                            </div>
                            <img src="${imageBase64}" 
                                 alt="Classified politician" 
                                 style="max-width: 300px; margin: 0 auto;">
                        </div>
                    `;
                    }
                    resultsDiv.classList.add('show');
                    
                } catch (error) {
                    resultsDiv.innerHTML = `<p style="color: #f44336;">Error: ${error.message}</p>`;
                    console.error('Classification error:', error);
                } finally {
                    // Reset button state
                    classifyBtn.disabled = false;
                    classifyBtn.textContent = 'Classify';
                }
            }

            // Helper function to convert file to base64
            function getBase64(file) {
                return new Promise((resolve, reject) => {
                    const reader = new FileReader();
                    reader.readAsDataURL(file);
                    reader.onload = () => resolve(reader.result);
                    reader.onerror = error => reject(error);
                });
            }

            classifyBtn.addEventListener('click', classifyImage);

            const politicians = [
                { name: "Nara Lokesh", image: "naralokesh.jpg" },
                { name: "Chandrababu Naidu", image: "chandrababu.jpg" },
                { name: "Y.S. Jagan Mohan Reddy", image: "jagan.jpg" },
                { name: "Scott Morrison", image: "scott.jpg" },
                { name: "Jacinda Ardern", image: "jacinda.jpg" },
                { name: "Justin Trudeau", image: "justin.jpg" },
                { name: "Olaf Scholz", image: "olaf.jpg" },
                { name: "Boris Johnson", image: "boris.jpg" },
                { name: "Arvind Kejriwal", image: "arvind.jpg" },
                { name: "Rahul Gandhi", image: "rahulgandhi.jpg" },
                { name: "Angela Merkel", image: "angela.jpg" },
                { name: "Y.S. Rajasekhara Reddy", image: "ysr.jpg" },
                { name: "Donald Trump", image: "trump.jpg" },
                { name: "Rishi Sunak", image: "rishisunak.jpg" },
                { name: "Volodymyr Zelensky", image: "zelensky.jpg" },
                { name: "Emmanuel Macron", image: "emmanuel.jpg" },
                { name: "Xi Jinping", image: "jinping.jpeg" },
                { name: "Vladimir Putin", image: "putin.jpg" },
                { name: "Joe Biden", image: "biden.jpg" },
                { name: "Narendra Modi", image: "modi.jpg" },
            ];

            // Function to dynamically generate the gallery
            function generateGallery() {
                const galleryGrid = document.querySelector(".gallery-grid");

                politicians.forEach((politician) => {
                    const galleryItem = document.createElement("div");
                    galleryItem.className = "gallery-item";

                    const img = document.createElement("img");
                    img.src = `images/${politician.image}`;
                    img.alt = politician.name;
                    img.loading = "lazy";

                    const p = document.createElement("p");
                    p.textContent = politician.name;

                    galleryItem.appendChild(img);
                    galleryItem.appendChild(p);
                    galleryGrid.appendChild(galleryItem);
                });
            }

            // Call the function when the DOM is loaded
            generateGallery();
        });