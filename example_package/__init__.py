from autoloader import load

__all__ = load(pattern='python_file_[01].py')

print(__all__)
