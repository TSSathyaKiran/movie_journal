import React, { useState } from 'react';

function Form(){
    const[movies, setMovies] = useState([])
    //state for the form inputs
    const[formData, setFormData] = useState({
        title: '',
        rating: '',
        review: ''
    })

    //state for handling validation errors
    const[error, setError] = useState('');
    //creating an event handler
    const handleChange = (e) => {
        const{ name, value } = e.target;
        setFormData(prevFormData => ({
            //prevFormData to access the current values in the field an use the spread operator and then assign new values if any
            ...prevFormData,
            [name]: value
        }));
    };

    //handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        if(!formData.rating.title || !formData.rating){
            setError('Movie Title and Rating are required')
            return; //stopping the function is the validation fails
        }

        if(isNaN(formData.rating) || formData.rating <1 || formData.rating > 10){
            setError('Stupid human being, rating is between 1 and 10')
            return;
        }

        //creating a new movie object with a unique id
        const newMovie = {
            id: Date.now(),
            ...formData
        };

        //update the movies list by adding the new movie
        setMovies(prevMovies => [newMovie, ...prevMovies]);

        //clear the form for next entry

        setFormData({title: '', rating: '', review: ''});
        setError(''); 
    };

    const deleteMovie = (idToDelete) => {
        setMovies(prevMovies => prevMovies.filter(movie => movie.id !== idToDelete));
    };

    //rendering
    return (
    <div className="bg-gray-900 text-white min-h-screen font-sans">
      <div className="container mx-auto p-4 md:p-8 max-w-3xl">
        
        {/* --- HEADER --- */}
        <header className="text-center mb-10">
          <h1 className="text-5xl font-bold text-yellow-400">Movie Journal</h1>
          <p className="text-gray-400 mt-2">Track and rate the films you've watched.</p>
        </header>

        <main>
          {/* --- FORM SECTION --- */}
          <div className="bg-gray-800 p-8 rounded-lg shadow-2xl mb-10">
            <h2 className="text-2xl font-semibold mb-6">Log a New Movie</h2>
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Movie Title Input */}
              <div>
                <label htmlFor="title" className="block text-sm font-medium text-gray-300 mb-2">Movie Title</label>
                <input
                  type="text"
                  id="title"
                  name="title"
                  value={formData.title}
                  onChange={handleChange}
                  placeholder="e.g., The Matrix"
                  className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-yellow-500"
                />
              </div>

              {/* Rating Input */}
              <div>
                <label htmlFor="rating" className="block text-sm font-medium text-gray-300 mb-2">Your Rating (1-10)</label>
                <input
                  type="number"
                  id="rating"
                  name="rating"
                  value={formData.rating}
                  onChange={handleChange}
                  placeholder="e.g., 9"
                  className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-yellow-500"
                />
              </div>

              {/* Review Textarea */}
              <div>
                <label htmlFor="review" className="block text-sm font-medium text-gray-300 mb-2">Your Review</label>
                <textarea
                  id="review"
                  name="review"
                  value={formData.review}
                  onChange={handleChange}
                  placeholder="What did you think?"
                  rows="4"
                  className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-yellow-500"
                ></textarea>
              </div>
              
              {/* Error Message Display */}
              {error && <p className="text-red-400 text-sm">{error}</p>}

              {/* Submit Button */}
              <button
                type="submit"
                className="w-full bg-yellow-500 hover:bg-yellow-600 text-gray-900 font-bold py-3 px-4 rounded-md transition duration-300 ease-in-out transform hover:scale-105"
              >
                Add Movie
              </button>
            </form>
          </div>

          {/* --- MOVIE LIST SECTION --- */}
          <div className="space-y-4">
            <h2 className="text-2xl font-semibold border-b border-gray-700 pb-2">Logged Movies ({movies.length})</h2>
            {movies.length > 0 ? (
              movies.map(movie => (
                <div key={movie.id} className="bg-gray-800 p-5 rounded-lg shadow-lg flex justify-between items-start">
                  <div>
                    <h3 className="text-xl font-bold text-yellow-400">{movie.title}</h3>
                    <p className="text-gray-300"><span className="font-semibold">Rating:</span> {movie.rating}/10</p>
                    {movie.review && <p className="text-gray-400 mt-2 italic">"{movie.review}"</p>}
                  </div>
                  <button 
                    onClick={() => deleteMovie(movie.id)}
                    className="text-gray-500 hover:text-red-400 transition-colors duration-200 text-xs font-semibold"
                  >
                    DELETE
                  </button>
                </div>
              ))
            ) : (
              <p className="text-gray-500 text-center py-4">No movies logged yet. Add one above!</p>
            )}
          </div>
        </main>
      </div>
    </div>
  );

}

export default Form;