var tags = {
    'calculus': {'verbose': 'Calculus', 'banner': 'primary'},
    'algebra': {'verbose': 'Algebra', 'banner': 'secondary'},
    'statistics': {'verbose': 'Statistics', 'banner': 'success'},
    'economics': {'verbose': 'Economics', 'banner': 'danger'},
    'astronomy': {'verbose': 'Astronomy', 'banner': 'warning'},
    'physics': {'verbose': 'Physics', 'banner': 'info'},
    'chemistry': {'verbose': 'Chemistry', 'banner': 'light'},
    'biology': {'verbose': 'Biology', 'banner': 'dark'},
    'comp': {'verbose': 'Computer Science', 'banner': 'primary'},
}

var tips = [
    ['Did you know?', 'It is extremely important to review your notes within 24 hours.'],
    ['A small tip:', 'Edit for words and phrases that don’t make sense. Write out abbreviated words that might be unclear later.'],
    ['Did you know?', 'Edit with a different colored font to distinguish between what you wrote in class and what you filled in later.'],
    ['A small tip:', 'Note all unfamiliar vocabulary or concepts you don’t understand (either on a seperate OpenStax Note or on the same one). This reminds you to look them up later.'],
]

var templates = {
    'default': {'verbose': 'Default Note', 'icon': 'file'},
    'cornell': {'verbose': 'Cornell Template', 'icon': 'file-alt'},
    'matrix': {'verbose': 'Matrix Template', 'icon': 'file-invoice'},
}

var auth = btoa('admin:admin');

var cmsurl = "http://localhost:8000"