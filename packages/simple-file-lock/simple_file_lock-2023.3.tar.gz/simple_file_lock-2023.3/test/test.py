#!/usr/bin/env python3

'''
Test the FileLock context manager.
'''

import multiprocessing
import pathlib
import tempfile
import time
import unittest

from simple_file_lock import FileLock


def test_locking(path, index):
    '''
    Test file locking. This is run via multiprocessing threads.
    '''
    with FileLock(path) as locked_path:
        content = str(index)
        locked_path.write_text(content, encoding='utf-8')
        time.sleep(0.2)
        return content == locked_path.read_text(encoding='utf-8')


class TestLockFile(unittest.TestCase):
    '''
    Test the FileLock context manager.
    '''

    def test_locking(self):
        '''
        Locking the path grants exclusive access.
        '''
        n_processes = 4
        with tempfile.TemporaryDirectory() as tmp_dir, \
                multiprocessing.Pool(n_processes) as pool:
            tmp_dir = pathlib.Path(tmp_dir).resolve()
            path = tmp_dir / 'test.txt'

            args = ((path, i) for i in range(n_processes))
            results = pool.starmap(test_locking, args)

            self.assertTrue(all(results))

    def test_return_value(self):
        '''
        The value returned by the context manager is the resolved path argument.
        '''
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_dir = pathlib.Path(tmp_dir).resolve()
            path = tmp_dir / 'test.txt'

            with FileLock(path) as locked_path:
                self.assertTrue(path.resolve() == locked_path.resolve())

    def test_dead_lock_removal(self):
        '''
        Dead locks are removed when the context is entered.
        '''
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_dir = pathlib.Path(tmp_dir).resolve()
            path = tmp_dir / 'test.txt'

            file_lock = FileLock(path)
            pid = file_lock.my_pid

            file_lock.my_pid = -1
            dead_lock = file_lock.create_lock()

            file_lock.my_pid = pid
            with file_lock:
                pass

            self.assertFalse(dead_lock.exists())


if __name__ == '__main__':
    unittest.main()
